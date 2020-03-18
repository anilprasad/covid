from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and - (minus) characters. e.g: john, john1, john-55a, etc.'
    )
    flags = 0
