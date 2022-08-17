from flask_restful import Resource

from flask import request

from managers.transactions import TransactionsManager


class CreateTransaction(Resource):
    def post(self):
        transaction = TransactionsManager.create(request.get_json())
        return transaction, 201