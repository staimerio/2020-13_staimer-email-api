# apps/urls.py

# Retic
from retic import App as app

# Constans
MAILGUN_SANDBOX = app.config.get('MAILGUN_SANDBOX')

# """Define all other apps"""
MAILGUN_BACKEND = {
    u"base_url": app.config.get('APP_MAILGUN_BACKEND'),
    u"messages": "/{0}/messages".format(MAILGUN_SANDBOX),
}


APP_BACKEND = {
    u"mailgun": MAILGUN_BACKEND,
}

"""Add Backend apps"""
app.use(APP_BACKEND, "backend")
