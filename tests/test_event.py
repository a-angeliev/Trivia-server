import json
from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from db import db
from managers.email import EmailSenderManager
from servvices.weather import WeatherInfo
from tests.factories import UsersFactory, RiddlesFactory
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

    @patch.object(EmailSenderManager, "send_email", return_value="some massage")
    @patch.object(WeatherInfo, "info", return_value=10)
    def test_create_event_and_actions(self, s, info_mock):
        """Testing end to end event point. Test by several steps:
        1. Correct create event
        2. Check information about current_event
        3. Start event action
        4. Passing correct answer to first question
        5. Passing incorrect answer to second question
        6. Passing correct answer to second question
        """
        url = "/riddles/0/events"

        user = UsersFactory()
        riddle = RiddlesFactory()

        token = generate_token(user)
        self.headers.update({"Authorization": f"Bearer {token}"})

        # 1. Correct create event
        resp = self.client.post(url, data=json.dumps({}), headers=self.headers)
        event_url = resp.json["url"][21:]
        assert resp.status_code == 201

        # 2. Check information about current_event
        resp = self.client.get(event_url)
        expected_resp = {
            "massage": "You should start the riddle. Once the riddle start there is no "
            "money refunds anymore.Wind is >5 km/h so we dont recommend to "
            "start riddle now."
        }
        assert resp.json == expected_resp

        # 3. Start event action
        resp = self.client.post(event_url, data=json.dumps({}), headers=self.headers)
        expected_resp = {"Question 1": "Qeustion1"}
        assert resp.json == expected_resp

        # 4. Passing correct answer to first question
        data = {"answer": "Answer1"}
        resp = self.client.post(event_url, data=json.dumps(data), headers=self.headers)
        expected_resp = {"Question 2": "Qeustion2"}
        assert resp.json == expected_resp

        # 5. Passing incorrect answer to second question
        data = {"answer": "Answer1"}
        resp = self.client.post(event_url, data=json.dumps(data), headers=self.headers)
        expected_resp = {"massage": "Wrong answer. Try something else."}
        assert resp.json == expected_resp

        # 6. Passing correct answer to second question
        data = {"answer": "Answer2"}
        resp = self.client.post(event_url, data=json.dumps(data), headers=self.headers)
        expected_resp = {"massage": "You finished the riddle for 0:00:00"}
        assert resp.json == expected_resp
