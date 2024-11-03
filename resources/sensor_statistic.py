from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.sensor_statistic import SensorStatisticManager
from models import RoleType


from sqlalchemy import func

from schemas.request.sensor_statistic import SensorStatisticRequestSchema
from schemas.response.sensor_statistic import SensorStatisticResponseSchema
from util.decorators import permission_required, validate_schema

class SensorStatisticListCreate(Resource):
    @auth.login_required
    def get(self):

        user = auth.current_user()
        sensor_datas = SensorStatisticManager.get_sensor_statistics(user)
        return {"sensor_statistics": SensorStatisticResponseSchema().dump(sensor_datas, many=True)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorStatisticRequestSchema)
    def post(self):

        data = request.get_json()
        user = auth.current_user()
        #data.setdefault('timestamp', func.now())
        SensorStatisticManager.create_sensor_statistic(user, data)
        return {'message': 'Sensor Statistic created successfully'}, 201


class SensorStatisticDetail(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def get(self, sensor_statistic_id):
        user = auth.current_user()
        room = SensorStatisticManager.get_sensor_statistic(user, sensor_statistic_id)
        return {"sensor_statistic": SensorStatisticResponseSchema().dump(room)}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    @validate_schema(SensorStatisticRequestSchema)
    def put(self, sensor_statistic_id):
        user = auth.current_user()
        data = request.get_json()
        SensorStatisticManager.update_sensor_statistic(user,sensor_statistic_id,data)
        return {'message': 'Sensor Statistic updated successfully'}, 200

    @auth.login_required
    @permission_required(RoleType.user)
    def delete(self, sensor_statistic_id):
        user = auth.current_user()
        SensorStatisticManager.delete_sensor_statistic(user,sensor_statistic_id)
        return {'message': 'Sensor Statistic deleted successfully'}, 200