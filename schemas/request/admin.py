from marshmallow import Schema, fields


class CreateAdminRequestSchema(Schema):
    email = fields.Email(required=True)
