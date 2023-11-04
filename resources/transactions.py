from flask_restful import Resource

from flask import request

from managers.auth import auth
from managers.transactions import TransactionsManager
from models import RoleType
from schemas.response.transactions import TransactionsAllResponseSchema
from util.decorators import permission_required


class CreateTransaction(Resource):
    def post(self):
        transaction = TransactionsManager.create(request.get_json())
        return transaction, 201

    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self):
        transactions = TransactionsManager.get_all()
        schema = TransactionsAllResponseSchema()
        return schema.dump(transactions, many=True)
