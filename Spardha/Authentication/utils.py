# from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from sendgrid.helpers.mail import (Mail,From)
from sendgrid import SendGridAPIClient
from django.conf import settings
from Spardha.settings import DEFAULT_FROM_EMAIL

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            # subject=data["email_subject"], body=data["email_body"], to=data["to_mail"],template_id=["template_id"],dynamic_template_data=["dynamic_template_data"]
            subject=data["email_subject"], body=data["email_body"], to=data["to_mail"]
        )
        email.template_id = data["template_id"]
        email.dynamic_template_data = data["dynamic_template_data"]
        email.content_subtype = "html"
        email.send(fail_silently=False)

    @staticmethod
    def send_email_sendgrid(data):
        print(DEFAULT_FROM_EMAIL)
        from_email = From(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER_NAME)
        email = Mail(from_email, to_emails=data["to_mail"])
        email.template_id = settings.SENDGRID_VERIFY_ACCOUNT_TEMP_ID
        email.dynamic_template_data = data["dynamic_template_data"]
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(email)
            code, headers = response.status_code, response.headers
            if code != 202:
                print(f"Response code: {code}")
            # print(f"Response headers: {headers}")
        except Exception as e:
                print("Error: {0}".format(e))
        return 1

