from werkzeug.exceptions import NotFound

from db import db
from models import UsersModel
from models.riddles import RiddlesModel
from util.decorators import check_length_questions_answers
from models.enums import State, RoleType

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
    def get_all(user):
        if isinstance(user, UsersModel):
            if user.role == RoleType.admin:
                return RiddlesModel.query.all()
        return RiddlesModel.query.filter_by(status=State.available).all()

    @staticmethod
    def get_by_id(user, id_):
        mapper = {
            RoleType.admin: RiddlesModel.query.filter_by(id=id_).first(),
            RoleType.user: RiddlesModel.query.filter_by(id=id_).filter_by(status=State.available).first()
        }
        if isinstance(user, UsersModel):
            if not mapper[user.role]:
                raise NotFound("This riddle does not exist.")
            return mapper[user.role]
