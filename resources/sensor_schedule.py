from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.sensor_schedule import SensorScheduleManager
from models import RoleType


from sqlalchemy import func

from schemas.request.sensor_schedule import SensorScheduleRequestSchema
from schemas.response.sensor_schedule import SensorScheduleResponseSchema
from util.decorators import permission_required, validate_schema

class SensorScheduleListCreate(Resource):
    @auth.login_required
    def get(self):

        user = auth.current_user()
        sensor_datas = SensorScheduleManager.get_sensor_schedules(user)
        return {"sensor_schedules": SensorScheduleResponseSchema().dump(sensor_datas, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorScheduleRequestSchema)
    def post(self):

        data = request.get_json()
        user = auth.current_user()
        data.setdefault('timestamp', func.now())
        SensorScheduleManager.create_sensor_schedule(user, data)
        return {'message': 'Sensor Schedule created successfully'}, 201


class SensorScheduleDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self, sensor_data_id):
        user = auth.current_user()
        room = SensorScheduleManager.get_sensor_schedule(user, sensor_data_id)
        return {"sensor_schedule": SensorScheduleResponseSchema().dump(room)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorScheduleRequestSchema)
    def put(self, sensor_data_id):
        user = auth.current_user()
        data = request.get_json()
        SensorScheduleManager.update_sensor_schedule(user,sensor_data_id,data)
        return {'message': 'Sensor Schedule updated successfully'}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    def delete(self, sensor_data_id):
        user = auth.current_user()
        SensorScheduleManager.delete_sensor_schedule(user,sensor_data_id)
        return {'message': 'Sensor Schedule deleted successfully'}, 200