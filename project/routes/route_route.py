from flask import Blueprint, Response, jsonify, make_response, request
from flasgger import swag_from
from http import HTTPStatus

from project.controllers import route_controller
from project.models import Route, User
from project.schemas.route_schema import RoutePostParamsSchema, RouteResponseSchema, RoutePatchParamsSchema

swag = {
    "tags": ["route"],
}

route_bp = Blueprint('route', __name__, url_prefix='/route')


#-------------------------- GET ALL --------------------------------------
@route_bp.get('')
@swag_from({
    **swag,
    "responses": {
        200: {"description": "Success request"},
    }
})
def get_all_routes() -> Response:
    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


#-------------------------- CREATE --------------------------------
@route_bp.post('/')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": RoutePostParamsSchema,
        }
    ],
    "responses": {
        201: {"description": "Successfully created"},
        404: {"description": "User does not exist"},
        409: {"description": "Route already exists"},
    }
})
def create_route() -> Response:
    content = request.get_json()
    
    if not User.query.get(content['user_id']):
        return make_response(jsonify({"message": "User does not exist"}), HTTPStatus.NOT_FOUND)

    if Route.query.filter_by(user_id=content["user_id"]).filter_by(name=content["name"]).first():
        return make_response(jsonify({"message": "Route already exists"}), HTTPStatus.CONFLICT)
    
    route = Route(**content)
    route_controller.create(route)
    return make_response("Route created", HTTPStatus.CREATED)


#-------------------------- GET BY ID --------------------------------
@route_bp.get('/<int:id>')
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
        200: {"description": "Success request", "schema": RouteResponseSchema},
        404: {"description": "Route not found"},
    }
})
def get_route(id: int) -> Response:
    return make_response(jsonify(route_controller.find_by_id(id)), HTTPStatus.OK)


#-------------------------- UPDATE --------------------------------
@route_bp.put('/<int:id>')
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
            "schema": RoutePostParamsSchema,
        }
        
    ],
    "responses": {
        200: {"description": "Route updated"},
        404: {"description": "Route not found"},
    }
})
def update_route(id: int) -> Response:
    content = request.get_json()
    route = Route(**content)
    route_controller.update(id, route)
    return make_response("Route updated", HTTPStatus.OK)


#-------------------------- PATCH --------------------------------
@route_bp.patch('/<int:id>')
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
            "schema": RoutePatchParamsSchema,
        }
        
    ],
    "responses": {
        200: {"description": "Route updated"},
        404: {"description": "Route not found"},
    }
})
def patch_route(id: int) -> Response:
    content = request.get_json()
    route_controller.patch(id, content)
    return make_response("Route updated", HTTPStatus.OK)


#-------------------------- DELETE --------------------------------
@route_bp.delete('/<int:id>')
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
        200: {"description": "Route deleted"},
        404: {"description": "Route not found"},
    }
})
def delete_route(id: int) -> Response:
    route_controller.delete(id)
    return make_response("Route deleted", HTTPStatus.OK)