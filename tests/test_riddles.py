import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UsersModel
from tests.factories import UsersFactory
from tests.helpers import generate_token


class TestAuth(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestConfig")

    def test_create_riddle(self):
        url = "/riddles"
        data = {
            "title": "second riddle",
            "description": "this is the first riddle for our project",
            "price": 10.0,
            "questions": "question 1@question2@question 3",
            "answers": "answer 1@ Answer2@Answer 3",
            "number_of_questions": 3,
        }

        admin = UsersFactory()
        token = generate_token(admin)
        self.headers.update({"Authorization": f"Bearer {token}"})

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        actual_resp = resp.json
        id = actual_resp["id"]
        status = actual_resp["status"]
        expected_resp = {"id": id, "status": status, "discount": 0.0, **data}

        assert resp.json == expected_resp

        users = UsersModel.query.all()
        assert len(users) == 1

        assert resp.status_code == 201
