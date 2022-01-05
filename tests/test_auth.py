import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UsersModel, RoleType
from tests.helpers import object_as_dict


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

    def test_register(self):
        """
        Test if a user is in database when register endpoin is hit.
        Assure that the role assign is a User role.
        """

        url = "/register"

        data = {"email": "test@test.com", "password": "12345a!"}

        users = UsersModel.query.all()
        assert len(users) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 201
        assert "token" in resp.json

        users = UsersModel.query.all()
        assert len(users) == 1
        user = object_as_dict(users[0])
        user.pop("password")
        data.pop("password")

        assert user == {"id": user["id"], "role": RoleType.user, **data}
