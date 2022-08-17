from flask_restful import Resource
from flask import request
from managers.discount import DiscountManager


class DiscountValidation(Resource):
    @staticmethod
    def post():
        discount_code = request.get_json()
        print(request.get_json())

        discount_is_valid = DiscountManager.is_valid(discount_code)
        print(discount_is_valid)
        return discount_is_valid

