
# Retic
from retic import Request, Response, Next

# Services
from retic.services.validations import validate_obligate_fields
from retic.services.responses import success_response_service, error_response_service
import services.mailgun.mailgun as mailgun


def send_email(req: Request, res: Response, next: Next):
    """Send a email"""

    """Validate all obligated params"""
    _validate = validate_obligate_fields({
        u'toaddr': req.param('toaddr'),
        u'fromaddr': req.param('fromaddr'),
        u'subject': req.param('subject'),
        u'body': req.param('body'),
    })

    """If it has any error, return an error message"""
    if _validate["valid"] is False:
        return res.bad_request(
            error_response_service(
                "The param {} is necesary.".format(_validate["error"])
            )
        )

    _send_email = mailgun.send_email(
        req.param('toaddr'),
        req.param('fromaddr'),
        req.param('subject'),
        req.param('body')
    )

    """Check it has any error"""
    if _send_email['valid'] is False:
        res.not_found(_send_email)
    else:
        res.ok(_send_email)
