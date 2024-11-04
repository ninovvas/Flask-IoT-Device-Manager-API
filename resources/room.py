
from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.room import RoomManager
from models import RoleType
from schemas.request.room import RoomRequestSchema
from schemas.response.room import RoomResponseSchema

from util.decorators import permission_required, validate_schema


class RoomListCreate(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self):

        user = auth.current_user()
        rooms = RoomManager.get_rooms()
        return {"homes": RoomResponseSchema().dump(rooms, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(RoomRequestSchema)
    def post(self):

        data = request.get_json()
        user = auth.current_user()
        RoomManager.create_room(data)
        return {'message': 'Room created successfully'}, 201


class RoomDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self, room_id):
        user = auth.current_user()
        room = RoomManager.get_room(user, room_id)
        return {"room": RoomResponseSchema().dump(room)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(RoomRequestSchema)
    def put(self, room_id):
        user = auth.current_user()
        data = request.get_json()
        RoomManager.update_room(user,room_id,data)
        return {'message': 'Room updated successfully'}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    def delete(self, room_id):
        user = auth.current_user()
        RoomManager.delete_room(user,room_id)
        return {'message': 'Room deleted successfully'}, 200