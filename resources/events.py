from flask import url_for, request
from flask_restful import Resource

from db import db
from managers.auth import auth, AuthManager
from managers.email import EmailSenderManager
from managers.events import EventsManager
from managers.riddles import RiddlesManager
from models import EventsModel
from schemas.response.events import CreateEventsResponseSchema


class CreateEvents(Resource):
    @auth.login_required
    def post(self, id_):
        user = auth.current_user()
        riddles = RiddlesManager.get_by_id(user, id_)
        token = AuthManager.encode_token(user)
        questions = riddles.questions
        answers = riddles.answers
        event = EventsManager.create(token=token, questions=questions,answers=answers)
        url = url_for("eventaction", token=token)
        final_url = "http://127.0.0.1:5000" + url
        EmailSenderManager.send_email(user.email, url)
        return {"url": final_url}


class EventAction(Resource):
    def get(self):
        token = request.args.get("token")
        result = EventsManager.event_current_state(token)
        return result

    def post(self):
        token = request.args.get("token")
        result = EventsManager.check_answer(token)
        return result
