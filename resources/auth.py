from datetime import datetime, timedelta

import flask
import jwt
# from Scripts import flask
from decouple import config
from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.users import UsersManager
from schemas import response
from schemas.request.users import UsersRegisterRequestSchema, UsersLoginRequestSchema
from util.decorators import validate_schema


def generate_token(user):
    payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=100)}
    return jwt.encode(payload, key=config("JWT_KEY"), algorithm="HS256")


class Register(Resource):
    @validate_schema(UsersRegisterRequestSchema)
    def post(self):
        user = UsersManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "userRole": user.role.value}, 201


class Login(Resource):
    @validate_schema(UsersLoginRequestSchema)
    def post(self):
        user = UsersManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "userRole": user.role.value, "email": user.email}, 200, {"Access-Control-Allow-Origin": "*"}

    # @validate_schema(UsersLoginRequestSchema)
    # def post(self):
    #     user = UsersManager.login(request.get_json())
    #     print(123)
    #     token = AuthManager.encode_token(user)
    #     response = flask.make_response({"token": token})
    #     response.headers['Access-Control-Allow-Origin'] = '*'
    #     print(response.headers)
    #     return response