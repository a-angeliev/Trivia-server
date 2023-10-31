from flask import url_for, request
from flask_restful import Resource

from managers.auth import auth, AuthManager
from managers.email import EmailSenderManager
from managers.events import EventsManager
from managers.riddles import RiddlesManager
from servvices.email import EmailSender


class CreateEvents(Resource):
    @auth.login_required
    def post(self, id_):
        user = auth.current_user()
        riddles = RiddlesManager.get_by_id(user, id_)
        token = AuthManager.encode_token(user)
        questions = riddles.questions
        answers = riddles.answers
        hint = riddles.hint
        event = EventsManager.create(token=token, questions=questions, answers=answers, hint=hint)
        url = url_for("eventaction", token=token)
        final_url = "http://localhost:3000" + url
        EmailSender.send(user.email, final_url, "This is link for access to the riddle!")
        return {"url": final_url}, 201


class EventAction(Resource):
    @staticmethod
    def get():
        token = request.args.get("token")
        result = EventsManager.event_current_state(token)
        return result

    @staticmethod
    def post():
        token = request.args.get("token")
        result = EventsManager.check_answer(token)
        return result

#hint logic
class EventHint(Resource):

    def get(self, current_question_):
        token = request.args.get("token")
        result = EventsManager.get_hint(token, current_question_)
        return result