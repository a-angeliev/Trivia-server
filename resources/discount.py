import json
from datetime import datetime

from flask_restful import Resource
from flask import request

from managers.auth import auth
from managers.discount import DiscountManager
from models import RoleType
from schemas.response.discount import DiscountListResponseSchema, DiscountCreateResponseSchema
from util.decorators import permission_required


class DiscountValidation(Resource):
    @staticmethod
    def post():
        discount_code = request.get_json()
        print(request.get_json())

        discount_is_valid = DiscountManager.is_valid(discount_code)
        print(discount_is_valid)
        return discount_is_valid


class ListDiscounts(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self):
        discounts = DiscountManager.get_all()
        schema = DiscountListResponseSchema()
        return schema.dumps(discounts, many=True), 200


    @auth.login_required
    @permission_required(RoleType.admin)
    def post(self):
        discount_data= request.get_json()
        print(discount_data)
        print(discount_data["started_on"])
        discount_data["started_on"] = datetime.strptime(discount_data['started_on'], '%Y-%m-%dT%H:%M:%S.%fZ')
        discount_data["ended_on"] = datetime.strptime(discount_data['ended_on'], '%Y-%m-%dT%H:%M:%S.%fZ')
        result = DiscountManager.create(discount_data)
        schema = DiscountCreateResponseSchema()
        return schema.dumps(result), 200

class EditDiscount(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, id_):
        discount_data = request.get_json()
        print(discount_data)
        print(discount_data["started_on"])
        discount_data["started_on"] = datetime.strptime(discount_data['started_on'], '%Y-%m-%dT%H:%M:%S.%fZ')
        discount_data["ended_on"] = datetime.strptime(discount_data['ended_on'], '%Y-%m-%dT%H:%M:%S.%fZ')
        updated_discount = DiscountManager.update(discount_data, id_)
        schema = DiscountCreateResponseSchema()
        return schema.dumps(updated_discount), 200

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, id_):
        result = DiscountManager.delete(id_)
        return result