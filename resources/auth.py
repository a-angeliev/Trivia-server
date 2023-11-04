from datetime import datetime, timedelta

import jwt

from decouple import config
from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.users import UsersManager
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
        print(request.get_json())
        user = UsersManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        response = {"token": token, "userRole": user.role.value, "email": user.email}
        return response, 200, {"Access-Control-Allow-Origin": "*"}
