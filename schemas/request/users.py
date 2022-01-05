from marshmallow import Schema, fields, validate

from util.validators import validate_password


class BaseUsersSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UsersRegisterRequestSchema(BaseUsersSchema):
    password = fields.String(
        required=True,
        validate=validate.And(validate.Length(min=5, max=60), validate_password),
    )


class UsersLoginRequestSchema(BaseUsersSchema):
    pass
