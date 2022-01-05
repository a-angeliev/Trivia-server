from marshmallow import ValidationError
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(numbers=1, special=1)


def validate_password(value):
    errors = policy.test(value)
    if errors:
        raise ValidationError("Not a valid password.")
