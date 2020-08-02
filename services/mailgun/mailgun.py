# Retic
from retic import env, App as app

# Requests
import requests

# Services
from retic.services.responses import success_response_service, error_response_service

# Constants
MAILGUN_KEY = app.config.get('MAILGUN_KEY')
MAILGUN_SANDBOX = app.config.get('MAILGUN_SANDBOX')

URL_SEND_MESSAGES = app.apps['backend']['mailgun']['base_url'] + \
    app.apps['backend']['mailgun']['messages']


def send_email(toaddr, fromaddr, subject, body, type='plain'):
    """Send an email to address

    :param toaddr: Address to send an email
    :param fromaddr: Adress that send the email
    :param subject: Subject of the email
    :param body: Body of the email
    """

    try:
        """Prepare payload"""
        _payload = {
            'from': fromaddr,
            'to': toaddr,
            'subject': subject,
            'html': body
        }
        """Send email"""
        _email_req = requests.post(
            URL_SEND_MESSAGES,
            auth=('api', MAILGUN_KEY),
            data=_payload
        )
        """Transform data response"""
        _email_json = _email_req.json()
        """Return data"""
        return success_response_service(
            data=_email_json,
            msg="Email send."
        )
    except Exception as err:
        return error_response_service(
            msg="Bad request."
        )
