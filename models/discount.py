from db import db


class DiscountModel(db.Model):
    __tablename__ = "discount"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    started_on = db.Column(db.DateTime, nullable=False)
    ended_on = db.Column(db.DateTime, nullable=False)
