from models import RoleType, RiddlesModel, State
from schemas.response.riddles import RiddlesCreateResponseUserSchema, RiddlesCreateResponseAdminSchema

mapper_role_schema = {
            RoleType.user: RiddlesCreateResponseUserSchema(),
            RoleType.admin: RiddlesCreateResponseAdminSchema()
        }


def mapper_role_query(id_):
    mapper_role_query = {
        RoleType.admin: RiddlesModel.query.filter_by(id=id_).first(),
        RoleType.user: RiddlesModel.query.filter_by(id=id_).filter_by(status=State.available).first()
    }
    return mapper_role_query