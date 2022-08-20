from marshmallow import Schema, fields


class TransactionsAllResponseSchema(Schema):
    id = fields.Integer(required = True)
    transactionId = fields.String(required = True)
    amount = fields.Float(required = True)
    description = fields.String(required = True)
    email = fields.String(required = True)
    update_time = fields.DateTime(required = True)