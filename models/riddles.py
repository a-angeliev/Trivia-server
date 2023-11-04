from db import db
from models.enums import State


class RiddlesModel(db.Model):
    __tablename__ = "riddles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0)
    status = db.Column(db.Enum(State), default=State.available, nullable=False)
    questions = db.Column(db.Text, nullable=False)
    answers = db.Column(db.Text, nullable=False)
    number_of_questions = db.Column(db.Integer, nullable=False)

    # new Columns
    duration = db.Column(db.String(255), nullable=True)
    where = db.Column(db.String(255), nullable=True)
    google_map = db.Column(db.Text, nullable=True)

    # adding code for hit
    hint = db.Column(db.Text, nullable=True)
