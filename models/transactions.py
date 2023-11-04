from db import db


class TransactionsModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    transactionId = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    update_time = db.Column(db.DateTime)
