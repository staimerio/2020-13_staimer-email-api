# Retic
from retic import Router

# Controllers
import controllers.email as email

"""Define all routes"""
router = Router()

"""Define routes for /emails"""
router.post("/emails", email.send_email)
