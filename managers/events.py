from datetime import datetime

from flask import request

from db import db
from models.events import EventsModel
from servvices.weather import WeatherInfo


class EventsManager:
    @staticmethod
    def create(**user_data):
        event = EventsModel(**user_data)
        db.session.add(event)
        db.session.flush()
        return event

    @staticmethod
    def get_hint(token, current_question):
        event = EventsModel.query.filter_by(token=token).first()
        hints = event.hint.split("@")
        hint = hints[current_question - 1]
        return hint

    @staticmethod
    def event_current_state(token):
        event = EventsModel.query.filter_by(token=token).first()
        if event.current_question == 0:
            try:
                wind = WeatherInfo.info()
                if wind < 5:
                    massage = "Wind is <5 km/h. Weather is good for riddles."
                else:
                    massage = (
                        "Wind is >5 km/h so we dont recommend to start riddle now."
                    )
                return {
                    "massage": f"Once you start it, you cannot get a refund and you cannot stop the game.{massage}"
                }
            except:
                return {
                    "massage": "Once you start it, you cannot get a refund and you cannot stop the game."
                }

        else:
            questions = [q for q in event.questions.split("@")]
            if event.current_question > len(questions):
                return {
                    "massage": f"You finished the riddle for {str(event.ended_on - event.started_on).split('.',2)[0]}",
                    "guessed_answer": event.guessed_answer,
                    "number_of_questions": questions.__len__(),
                    "end": "1",
                }
            return {
                f"question": questions[event.current_question - 1],
                "current_question": event.current_question,
                "guessed_answer": event.guessed_answer,
                "number_of_questions": questions.__len__(),
            }

    @staticmethod
    def check_answer(token):
        event = EventsModel.query.filter_by(token=token).first()
        if event.current_question == 0:
            event.current_question = 1
            event.started_on = datetime.utcnow()
            db.session.add(event)
            db.session.flush()
            return EventsManager.event_current_state(token)
        answer = request.get_json()
        answers = [a for a in event.answers.split("@")]

        if "skip" in answer:
            event.current_question += 1
            if event.current_question > len(answers):
                event.ended_on = datetime.utcnow()
            db.session.add(event)
            db.session.flush()
            return EventsManager.event_current_state(token)

        if event.current_question > len(answers):
            return EventsManager.event_current_state(token)

        if answer["answer"] == answers[event.current_question - 1]:
            event.current_question += 1
            event.guessed_answer += 1
            if event.current_question > len(answers):
                event.ended_on = datetime.utcnow()
            db.session.add(event)
            db.session.flush()
            return EventsManager.event_current_state(token)
        return {"massage": "Wrong answer. Try something else."}
