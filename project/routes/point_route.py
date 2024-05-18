from flask import Blueprint, Response, jsonify, make_response, request
from flasgger import swag_from
from http import HTTPStatus

from project.controllers import point_controller
from project.models import Route, Point
from project.schemas.point_schema import PointPostParamsSchema, PointResponseSchema, PointPatchParamsSchema

swag = {
    "tags": ["point"],
}

point_bp = Blueprint('point', __name__, url_prefix='/point')


#-------------------------- GET ALL --------------------------------------
@point_bp.get('')
@swag_from({
    **swag,
    "responses": {
        200: {"description": "Success request", "schema": PointResponseSchema},
    }
})
def get_all_points() -> Response:
    return make_response(jsonify(point_controller.find_all()), HTTPStatus.OK)


#-------------------------- CREATE --------------------------------
@point_bp.post('/')
@swag_from({
    **swag,
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": PointPostParamsSchema,
        }
    ],
    "responses": {
        201: {"description": "Successfully created"},
        404: {"description": "Route does not exist"},
    }
})
def create_point() -> Response:
    content = request.get_json()

    if not Route.query.get(content['route_id']):
        return make_response(jsonify({"message": "Route does not exist"}), HTTPStatus.NOT_FOUND)

    point = Point(**content)
    point_controller.create(point)
    return make_response("Point created", HTTPStatus.CREATED)


#-------------------------- GET BY ID --------------------------------
@point_bp.get('/<int:id>')
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
        200: {"description": "Success request", "schema": PointResponseSchema},
        404: {"description": "Point not found"},
    }
})
def get_point(id: int) -> Response:
    return make_response(jsonify(point_controller.find_by_id(id)), HTTPStatus.OK)


#-------------------------- UPDATE --------------------------------
@point_bp.put('/<int:id>')
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
            "schema": PointPostParamsSchema,
        }
        
    ],
    "responses": {
        200: {"description": "Point updated"},
        404: {"description": "Point not found"},
    }
})
def update_point(id: int) -> Response:
    content = request.get_json()
    point = Point(**content)
    point_controller.update(id, point)
    return make_response("Point updated", HTTPStatus.OK)


#-------------------------- PATCH --------------------------------
@point_bp.patch('/<int:id>')
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
            "schema": PointPatchParamsSchema,
        }
        
    ],
    "responses": {
        200: {"description": "Point updated"},
        404: {"description": "Point not found"},
    }
})
def patch_point(id: int) -> Response:
    content = request.get_json()
    point_controller.patch(id, content)
    return make_response("Point updated", HTTPStatus.OK)


#-------------------------- DELETE --------------------------------
@point_bp.delete('/<int:id>')
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
        200: {"description": "Point deleted"},
        404: {"description": "Point not found"},
    }
})
def delete_point(id: int) -> Response:
    point_controller.delete(id)
    return make_response("Point deleted", HTTPStatus.OK)