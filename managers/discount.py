import json
from datetime import datetime

from db import db
from models.discount import DiscountModel


class DiscountManager():
    @staticmethod
    def create(**discount_data):
        discount = DiscountModel(**discount_data)
        db.session.add(discount)
        db.session.flush()
        return discount

    @staticmethod
    def is_valid(discount_data):
        discount_data = json.loads(discount_data)
        # print(discount_data["discount_code"])
        discount = DiscountModel.query.filter_by(code=discount_data["discount_code"]).first()
        if discount:
            if datetime.utcnow() > discount.started_on and datetime.utcnow() < discount.ended_on:
                return {"is_valid": True, "discount": discount.discount}
        return {"is_valid": False}