from marshmallow import Schema, fields, validate


class BaseUsersSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=5, max=60))


class UsersRegisterRequestSchema(BaseUsersSchema):
    pass


class UsersLoginRequestSchema(BaseUsersSchema):
    pass
