from django.db import models
from project.models.CodeGenerator import CodeGenerator
from core.exceptions import CodeOrTokenNotExpired
import pytz
from datetime import datetime, timedelta

class Authorization(models.Model):
    code = models.IntegerField(null=True)
    code_created = models.DateTimeField(null=True)
    is_authorized = models.BooleanField(default=False)
    email_token = models.CharField(max_length=81)
    email_confirmed = models.BooleanField(default=False)
    email_token_created = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.is_authorized)

    class Meta:
        verbose_name = 'Authorization'
        verbose_name_plural = 'Authorizations'

    def generate_sms_code_and_save(self, digits, expired_in_minutes):
        # generate only a new sms code if the previous is expired
        if not self.code_created or not self.is_in_time(self.code_created, expired_in_minutes):
            code = CodeGenerator().generate_number_code(digits)
            self.code = code
            self.code_created = datetime.now()
            self.save()
            return code
        else:
            raise CodeOrTokenNotExpired()

    def generate_email_token_and_save(self, digits, expired_in_minutes):
        # generate only a new email code if the previous is expired
        if not self.email_token_created or not self.is_in_time(self.email_token_created, 1):
            token = CodeGenerator().generate_number_code(digits)
            self.email_token = token
            self.email_token_created = datetime.now()
            self.save()
            return token
        else:
            raise CodeOrTokenNotExpired()

    @staticmethod
    def is_in_time(created, time):
        three_minutes_left = datetime.now() - timedelta(minutes=time)
        three_minutes_left = three_minutes_left.replace(tzinfo=pytz.utc)
        code_created = created.replace(tzinfo=pytz.utc)
        if code_created > three_minutes_left:
            return True
        return False
