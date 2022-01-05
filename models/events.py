from datetime import datetime, timedelta

from sqlalchemy import func

from db import db


class EventsModel(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False)
    questions = db.Column(db.Text, nullable=False)
    answers = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    started_on = db.Column(db.DateTime)
    ended_on = db.Column(db.DateTime)
    refund_window = db.Column(
        db.DateTime, default=(datetime.utcnow() + timedelta(days=15))
    )
    current_question = db.Column(db.Integer, default=0)
