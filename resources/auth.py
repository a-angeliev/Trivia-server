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
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(UsersLoginRequestSchema)
    def post(self):
        user = UsersManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
