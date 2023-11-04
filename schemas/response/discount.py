from marshmallow import Schema, fields


class DiscountIsValidResponseSchema(Schema):
    token = fields.String(required=True)
    questions = fields.String(required=True)
    answers = fields.String(required=True)
    current_question = fields.Integer(required=True)


class DiscountListResponseSchema(Schema):
    id = fields.Integer(required=True)
    code = fields.String(required=True)
    discount = fields.Integer(required=True)
    started_on = fields.DateTime(required=True)
    ended_on = fields.DateTime(required=True)


class DiscountCreateResponseSchema(DiscountListResponseSchema):
    pass
