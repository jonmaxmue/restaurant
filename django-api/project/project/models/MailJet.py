from django.conf import settings
import requests
import json
import re
from mailjet_rest import Client
from core.exceptions import EmailOrSMSNotSend


class MailJet:

    def __init__(self):
        self.mail_api = Client(auth=(settings.MAILJET_MAIL_API_KEY, settings.MAILJET_MAIL_API_SECRET), version='v3.1')
        self.from_email = "dev@lunity.online"
        self.from_name = "lunity.online"

    @staticmethod
    def mailjet_sms_send(params):
        try:
            mailjet_sms_response = requests.post(
                settings.MAILJET_MAIL_API_URL,
                data=json.dumps(params),
                headers={
                    "Authorization": "Bearer " + settings.MAILJET_SMS_API_SECRET,
                    "content-type": "application/json"
                },
            )
            return mailjet_sms_response
        except Exception as e:
            raise e

    def send_mail_with_token(self, to_email, to_name, token):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.from_email,
                        "Name": self.from_name
                    },
                    "To": [
                        {
                            "Email": to_email,
                            "Name": to_name
                        }
                    ],
                    "Subject": "Token",
                    "TextPart": "Hier ist dein Token, um deine Handynummer aktualisieren zu können. ".join(token),
                    "HTMLPart": "<h3>Hier ist dein Token, um deine Handynummer aktualisieren zu können: </h3><br>" + token
                }
            ]
        }
        result = self.mail_api.send.create(data=data)
        if not result.ok:
            raise EmailOrSMSNotSend()

    def send_mail_with_update_message(self, to_email, to_name, message):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.from_email,
                        "Name": self.from_name
                    },
                    "To": [
                        {
                            "Email": to_email,
                            "Name": to_name
                        }
                    ],
                    "Subject": "Aktualisierung",
                    "TextPart": message,
                    "HTMLPart": message
                }
            ]
        }
        result = self.mail_api.send.create(data=data)
        return result.status_code

    @staticmethod
    def send_sms_with_code(number, code):
        mailjet_sms_response = MailJet.mailjet_sms_send({
            "From": "lunity",
            "To": "+49" + re.sub(r"\W+", '', number)[1:],
            "Text": "Hi, hier ist dein Code für lunity! Code: " + re.sub(r"\W+", '', code)
        })
        if not mailjet_sms_response.ok:
            raise EmailOrSMSNotSend()
