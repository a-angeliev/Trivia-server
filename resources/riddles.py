from flask import request
from flask_restful import Resource

from managers.auth import auth, AuthManager
from managers.riddles import RiddlesManager
from models.enums import RoleType
from schemas.request.riddles import RiddlesCreateRequestSchema
from schemas.response.riddles import RiddlesCreateResponseSchema
from util.decorators import validate_schema, permission_required


class ListCreateRiddle(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        riddles = RiddlesManager.get_all(user)
        schema = RiddlesCreateResponseSchema()
        return schema.dump(riddles, many=True)

    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RiddlesCreateRequestSchema)
    def post(self):
        riddle = RiddlesManager.create(request.get_json())
        schema = RiddlesCreateResponseSchema()
        return schema.dump(riddle)


class RiddleDetails(Resource):
    @auth.login_required
    def get(self, id_):
        user = auth.current_user()
        riddles = RiddlesManager.get_by_id(user, id_)
        schema = RiddlesCreateResponseSchema()
        return schema.dump(riddles)

    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RiddlesCreateRequestSchema)
    def put(self, id_):
        updated_riddle = RiddlesManager.update(request.get_json(), id_)
        schema = RiddlesCreateResponseSchema()
        return schema.dump(updated_riddle)

    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, id_):
        RiddlesManager.delete(id_)
        return {"message": "Success"}, 204
