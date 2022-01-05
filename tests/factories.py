import factory

from db import db
from models import UsersModel, RoleType, RiddlesModel, State


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class UsersFactory(BaseFactory):
    class Meta:
        model = UsersModel

    id = factory.Sequence(lambda u: u)
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.admin


class RiddlesFactory(BaseFactory):
    class Meta:
        model = RiddlesModel

    id = factory.Sequence(lambda u: u)
    title = "title"
    description = "description"
    price = 10
    status = State.available
    questions = "Qeustion1@Qeustion2"
    answers = "Answer1@Answer2"
    number_of_questions = 2
