from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.riddles import RiddlesManager
from models.enums import RoleType
from schemas.request.riddles import RiddlesCreateRequestSchema
from schemas.response.riddles import RiddlesCreateResponseSchema
from util.decorators import validate_schema, permission_required


class ListCreateRiddle(Resource):
    def get(self):
        # TODO add logic for diffrent roles
        riddles = RiddlesManager.get_all()
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
    def get(self, id_):
        pass

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
