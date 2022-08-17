from db import db


class FaqModel(db.Model):
    __tablename__ = "faq"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)