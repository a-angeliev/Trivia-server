from datetime import datetime

from flask import request

from db import db
from models.events import EventsModel


class EventsManager:
    @staticmethod
    def create(**user_data):
        event= EventsModel(**user_data)
        db.session.add(event)
        db.session.commit()
        return event


    @staticmethod
    def event_current_state(token):
        event = EventsModel.query.filter_by(token=token).first()
        if event.current_question == 0:
            return {"massage": "You should start the riddle. Once the riddle start there is no money refunds anymore."}
        else:
            questions = [q for q in event.questions.split("@")]
            if event.current_question > len(questions):
                return {"massage":f"You finished the riddle for {str(event.ended_on - event.started_on).split('.',2)[0]}"}
            return {f"Question {event.current_question }": questions[event.current_question - 1]}

    @staticmethod
    def check_answer(token):
        event = EventsModel.query.filter_by(token=token).first()
        if event.current_question == 0:
            event.current_question = 1
            event.started_on = datetime.utcnow()
            db.session.add(event)
            db.session.commit()
            return EventsManager.event_current_state(token)
        answer = request.get_json()
        answers = [a for a in event.answers.split("@")]
        if event.current_question > len(answers):
            return EventsManager.event_current_state(token)
        if answer["answer"] == answers[event.current_question-1]:
            event.current_question += 1
            if event.current_question > len(answers):
                event.ended_on = datetime.utcnow()
            db.session.add(event)
            db.session.commit()
            return EventsManager.event_current_state(token)
        return {"massage": "Wrong answer. Try something else."}
