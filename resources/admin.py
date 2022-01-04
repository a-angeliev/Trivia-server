from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.users import UsersManager
from models import RoleType
from schemas.request.admin import CreateAdminRequestSchema
from util.decorators import permission_required, validate_schema


class CreateAdmin(Resource):

    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(CreateAdminRequestSchema)
    def post(self):
        UsersManager.create_admin(request.get_json())
        return 201