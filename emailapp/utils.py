from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_custom_email(email):
    # Check email format
    pattern = r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com)$'
    if not re.match(pattern, email, re.IGNORECASE):
        raise ValidationError(_('Invalid email format. Only Gmail and Yahoo Mail addresses are allowed.'))

    # Extract local part and domain
    local_part, domain = email.split('@')

    # Additional checks for Gmail
    if domain.lower() == 'gmail.com':
        # Gmail username rules:
        # - 6-30 characters long
        # - Can contain letters (a-z), numbers, and periods
        # - Must start and end with a letter or number
        # - Cannot have two periods in a row
        gmail_pattern = r'^[a-z0-9][a-z0-9.]{4,28}[a-z0-9]$'
        if not re.match(gmail_pattern, local_part, re.IGNORECASE):
            raise ValidationError(_('Invalid Gmail address format.'))
        if '..' in local_part:
            raise ValidationError(_('Gmail addresses cannot contain two consecutive periods.'))

    # Additional checks for Yahoo Mail
    elif domain.lower() == 'yahoo.com':
        # Yahoo Mail username rules:
        # - 4-32 characters long
        # - Can contain letters (a-z), numbers, underscores, and periods
        # - Must start with a letter or number
        yahoo_pattern = r'^[a-z0-9][a-z0-9_.]{2,30}[a-z0-9]$'
        if not re.match(yahoo_pattern, local_part, re.IGNORECASE):
            raise ValidationError(_('Invalid Yahoo Mail address format.'))

    return email