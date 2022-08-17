import json

from db import db
from models.transactions import TransactionsModel


class TransactionsManager:
    @staticmethod
    def create(transaction_data):
        transaction_data = json.loads(transaction_data)
        print(transaction_data)
        transaction = TransactionsModel(**transaction_data)
        db.session.add(transaction)
        db.session.flush()
        return {"status": "create"}, 201