import json
from datetime import datetime

from werkzeug.exceptions import NotFound

from db import db
from models.discount import DiscountModel


class DiscountManager:
    @staticmethod
    def create(discount_data):
        discount = DiscountModel(**discount_data)
        db.session.add(discount)
        db.session.flush()
        return discount

    @staticmethod
    def update(discount_data, id_):
        discount_q = DiscountModel.query.filter_by(id = id_)
        discount = discount_q.first()
        if not discount:
            raise NotFound("This discount does not exist.")

        discount_q.update(discount_data)
        db.session.add(discount)
        db.session.flush()
        return discount

    @staticmethod
    def delete(id_):
        discount = DiscountModel.query.filter_by(id = id_).first()
        if not discount:
            raise NotFound("This discount does not exist.")

        db.session.delete(discount)
        db.session.flush()
        return 200

    @staticmethod
    def is_valid(discount_data):
        discount_data = json.loads(discount_data)
        # print(discount_data["discount_code"])
        discount = DiscountModel.query.filter_by(code=discount_data["discount_code"]).first()
        if discount:
            if datetime.utcnow() > discount.started_on and datetime.utcnow() < discount.ended_on:
                return {"is_valid": True, "discount": discount.discount}
        return {"is_valid": False}

    @staticmethod
    def get_all():
        return DiscountModel.query.all()