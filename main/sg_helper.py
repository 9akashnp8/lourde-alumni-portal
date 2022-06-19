import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
from environs import Env

env = Env()
env.read_env()

def sendEmail(message):
    try:
        sendgrid_client = SendGridAPIClient(env.str('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
    except Exception as e:
        print(response.status_code)
        print(response.body)
        print(response.headers)

def applicationEmail(email, name, application_no, url):
    to_emails = [
        To(email=email,
        name=name,
        dynamic_template_data={
            'name': name,
            'application_no': application_no,
            'url': url
        },
        )
    ]
    message = Mail(
        from_email=(env.str("from_email"), 'Lourde Alumni Association'),
        to_emails=to_emails,)
    message.template_id = 'd-d49ca538d1cd4fef850c5acc36010d06'

    sendEmail(message=message)

def alumniEmail(email, name, alumni_no):
    to_emails = [
        To(email=email,
        name=name,
        dynamic_template_data={
            'name': name,
            'alumni_no': alumni_no,
        },
        )
    ]
    message = Mail(
        from_email=(env.str("from_email"), 'Lourde Alumni Association'),
        to_emails=to_emails,)
    message.template_id = 'd-bbfe2ebc64d140c29d8a0955e85fdbe0'

    sendEmail(message=message)