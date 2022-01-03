from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if errors:
                raise BadRequest(errors)
            return func(*args, **kwargs)

        return decorated_func

    return wrapper


def permission_required(permission):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            user = auth.current_user()
            if not user.role == permission:
                raise Forbidden("You dont have access to this resource")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper


def check_length_questions_answers(func):
    def wapper(riddle_data):
        questions_length = len([x for x in riddle_data["questions"].split("@")])
        answer_length = len([x for x in riddle_data["answers"].split("@")])
        if not questions_length == answer_length:
            raise BadRequest("The questions and the answers should be the same number")
        return func(riddle_data)

    return wapper
