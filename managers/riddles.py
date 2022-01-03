from werkzeug.exceptions import NotFound

from db import db
from models.riddles import RiddlesModel
from util.decorators import check_length_questions_answers


class RiddlesManager:
    @staticmethod
    @check_length_questions_answers
    def create(riddle_data):
        riddle = RiddlesModel(**riddle_data)
        db.session.add(riddle)
        db.session.commit()
        return riddle

    @staticmethod
    def update(riddle_data, id_):
        riddle_q = RiddlesModel.query.filter_by(id=id_)
        riddle = riddle_q.first()
        if not riddle:
            raise NotFound("This riddle does not exist.")

        riddle_q.update(riddle_data)
        db.session.add(riddle)
        db.session.commit()
        return riddle

    @staticmethod
    def delete(id_):
        riddle_q = RiddlesModel.query.filter_by(id=id_)
        riddle = riddle_q.first()
        if not riddle:
            raise NotFound("This riddle does not exist.")

        db.session.delete(riddle)
        db.session.commit()

    @staticmethod
    def get_all():
        return RiddlesModel.query.all()
