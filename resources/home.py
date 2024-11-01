from flask import request
from flask_restful import Resource
from managers.auth import auth
from models.enums import RoleType
from managers.device_manager import DeviceManager
from schemas.request.home import HomeRequestSchema
from schemas.response.home import HomeResponseSchema
from util.decorators import permission_required, validate_schema


class HomeListCreate(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        homes = DeviceManager.get_homes(user)
        return {"homes": HomeResponseSchema().dump(homes, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(HomeRequestSchema)
    def post(self):
        data = request.get_json()
        user = auth.current_user()
        DeviceManager.create_home(user,data)
        return {'message': 'Home created successfully'}, 201
