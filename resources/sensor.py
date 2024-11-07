
from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.sensor import SensorManager
from models import RoleType
from schemas.request.sensor import SensorRequestSchema
from schemas.response.sensor import SensorResponseSchema
from util.decorators import permission_required, validate_schema


class SensorListCreate(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self):

        user = auth.current_user()
        sensors = SensorManager.get_sensors(user)
        return {"sensors": SensorResponseSchema().dump(sensors, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorRequestSchema)
    def post(self):

        data = request.get_json()
        user = auth.current_user()
        SensorManager.create_sensor(user, data)
        return {'message': 'Sensor created successfully'}, 201


class SensorDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self, sensor_id):
        user = auth.current_user()
        sensor = SensorManager.get_sensor(user, sensor_id)
        return {"sensor": SensorResponseSchema().dump(sensor)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorRequestSchema)
    def put(self, sensor_id):
        user = auth.current_user()
        data = request.get_json()
        SensorManager.update_sensor(user,sensor_id,data)
        return {'message': 'Sensor updated successfully'}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    def delete(self, sensor_id):
        user = auth.current_user()
        SensorManager.delete_sensor(user,sensor_id)
        return {'message': 'Sensor deleted successfully'}, 200