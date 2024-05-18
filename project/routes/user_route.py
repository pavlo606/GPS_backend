from flask import Blueprint, Response, jsonify, make_response, request
from flasgger import swag_from
from http import HTTPStatus

from project.controllers import user_controller
from project.models import User
from project.schemas.user_schema import RegistrationSchema, UserResponseSchema, UserPatchSchema, LoginSchema

swag = {
    "tags": ["user"],
}

user_bp = Blueprint('user', __name__, url_prefix='/user')


# #-------------------------- GET ALL --------------------------------------
# @user_bp.get('')
# @swag_from({
#     **swag,
#     "responses": {
#         200: {"description": "Success request"},
#     }
# })
# def get_all_users() -> Response:
#     return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)


#-------------------------- LOGIN --------------------------------
@user_bp.post('/login')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": LoginSchema,
        }
    ],
    "responses": {
        200: {"description": "Login successful"},
        401: {"description": "Invalid credentials"},
    }
})
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user: User = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        return make_response("Login successful", HTTPStatus.OK)
    else:
        return make_response("Invalid credentials", HTTPStatus.UNAUTHORIZED)


#-------------------------- REGISTER --------------------------------
@user_bp.post('/register')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": RegistrationSchema,
        }
    ],
    "responses": {
        201: {"description": "Successfull registration"},
        409: {"description": "User already exists"},
    }
})
def registration() -> Response:
    content = request.get_json()
    
    if User.query.filter_by(username=content['username']).first():
        return make_response('User with this name already exists', HTTPStatus.CONFLICT)
    if User.query.filter_by(email=content['email']).first():
        return make_response('User with this email already exists', HTTPStatus.CONFLICT)
    
    user = User(**content)
    user_controller.create(user)
    return make_response("Successfull registration", HTTPStatus.CREATED)


# #-------------------------- GET BY ID --------------------------------
# @user_bp.get('/<int:id>')
# @swag_from({
#     **swag,
#     "parameters": [
#         {
#             "name": "id",
#             "in": "path",
#             "type": "integer",
#             "required": "true",
#         }
#     ],
#     "responses": {
#         200: {"description": "Success request", "schema": UserResponseSchema},
#         404: {"description": "User not found"},
#     }
# })
# def get_user(id: int) -> Response:
#     return make_response(jsonify(user_controller.find_by_id(id)), HTTPStatus.OK)


#-------------------------- UPDATE --------------------------------
@user_bp.put('/<int:id>')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": "true",
        },
        {
            "name": "body",
            "in": "body",
            "schema": RegistrationSchema,
        }
        
    ],
    "responses": {
        200: {"description": "User updated"},
        404: {"description": "User not found"},
    }
})
def update_user(id: int) -> Response:
    content = request.get_json()
    user = User(**content)
    user_controller.update(id, user)
    return make_response("User updated", HTTPStatus.OK)


#-------------------------- PATCH --------------------------------
@user_bp.patch('/<int:id>')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": "true",
        },
        {
            "name": "body",
            "in": "body",
            "schema": UserPatchSchema,
        }
        
    ],
    "responses": {
        200: {"description": "User updated"},
        404: {"description": "User not found"},
    }
})
def patch_user(id: int) -> Response:
    content = request.get_json()
    user_controller.patch(id, content)
    return make_response("User updated", HTTPStatus.OK)


#-------------------------- DELETE --------------------------------
@user_bp.delete('/<int:id>')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": "true",
        }
    ],
    "responses": {
        200: {"description": "User deleted"},
        404: {"description": "User not found"},
    }
})
def delete_user(id: int) -> Response:
    user_controller.delete(id)
    return make_response("User deleted", HTTPStatus.OK)