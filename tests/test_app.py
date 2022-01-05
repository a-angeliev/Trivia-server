import json

from flask_testing import TestCase

from config import create_app
from db import db


class TestApplication(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return create_app("config.TestConfig")

    def test_authentication_missing_auth_header_raises(self):
        url_methods = [
            ("/riddles", "GET"),
            ("/riddles", "POST"),
            ("/riddles/1", "GET"),
            ("/riddles/1", "PUT"),
            ("/riddles/1", "DELETE"),
            ("/riddles/1/events", "POST"),
            ("/admin", "POST"),
        ]

        for url, method in url_methods:
            if method == "GET":
                resp = self.client.get(url)
            elif method == "POST":
                resp = self.client.post(url, data=json.dumps({}))
            elif method == "PUT":
                resp = self.client.put(url, data=json.dumps({}))
            else:
                resp = self.client.delete(url)

            assert resp.status_code == 400
            assert resp.json == {"message": "Invalid Token"}

    def test_permission_request_endpoits_admin_access_raises(self):
        pass
