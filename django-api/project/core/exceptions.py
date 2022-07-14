from rest_framework.exceptions import APIException


class CodeOrTokenNotExpired(APIException):
    status_code = 403
    default_detail = "Bitte in ein paar Minuten nochmal versuchen"


class TokenOrIdFailed(APIException):
    status_code = 401
    default_detail = "Hast du den Token richtig eingegeben?"


class UserNotExsists(APIException):
    status_code = 400
    default_detail = "Diese Handynummer ist nicht registriert."


class EmailNotInserted(APIException):
    status_code = 400
    default_detail = "Deine Emailadresse ist nicht eingetragen."


class EmailOrSMSNotSend(APIException):
    status_code = 400
    default_detail = "Die Nachricht konnte nicht gesendet werden. Ist deine Eingabe richtig?"


