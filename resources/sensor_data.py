from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.sensor_data import SensorDataManager
from models import RoleType
from schemas.request.sensor_data import SensorDataRequestSchema
from schemas.response.sensor_data import SensorDataResponseSchema

from sqlalchemy import func

from util.decorators import permission_required, validate_schema

class SensorDataListCreate(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self):

        user = auth.current_user()
        sensor_datas = SensorDataManager.get_sensor_datas(user)
        return {"sensor_data": SensorDataResponseSchema().dump(sensor_datas, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorDataRequestSchema)
    def post(self):

        data = request.get_json()
        user = auth.current_user()
        data.setdefault('timestamp', func.now())
        SensorDataManager.create_sensor_data(user, data)
        return {'message': 'Sensor Data created successfully'}, 201


class SensorDataDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self, sensor_data_id):
        user = auth.current_user()
        room = SensorDataManager.get_sensor_data(user, sensor_data_id)
        return {"sensor_data": SensorDataResponseSchema().dump(room)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorDataRequestSchema)
    def put(self, sensor_data_id):
        user = auth.current_user()
        data = request.get_json()
        SensorDataManager.update_sensor_data(user,sensor_data_id,data)
        return {'message': 'Sensor Data updated successfully'}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    def delete(self, sensor_data_id):
        user = auth.current_user()
        SensorDataManager.delete_sensor_data(user,sensor_data_id)
        return {'message': 'Sensor Data deleted successfully'}, 200