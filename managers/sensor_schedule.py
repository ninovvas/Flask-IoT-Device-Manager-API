from managers.base import BaseManager
from models import SensorScheduleModel


class SensorScheduleManager:

    @staticmethod
    def get_sensor_schedules(user):
        return BaseManager.get_items(user, SensorScheduleModel)

    @staticmethod
    def create_sensor_schedule(user, data):
        data["user_id"] = user.id

        BaseManager.create_item(SensorScheduleModel, data)

    @staticmethod
    def get_sensor_schedule(user, sensor_schedule_id):
        return BaseManager.get_item(user=user, db_model=SensorScheduleModel, item_id=sensor_schedule_id, error_msg="Sensor Schedule")

    @staticmethod
    def update_sensor_schedule(user, sensor_schedule_id, data):

        BaseManager.update_item(user=user, db_model=SensorScheduleModel, item_id=sensor_schedule_id, data=data,
            error_msg="Sensor Schedule")

    @staticmethod
    def delete_sensor_schedule(user, sensor_schedule_id):
        BaseManager.delete_item(user=user, db_model=SensorScheduleModel, item_id=sensor_schedule_id, error_msg="Sensor Schedule")