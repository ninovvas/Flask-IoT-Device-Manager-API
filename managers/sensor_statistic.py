from managers.base import BaseManager
from models import SensorStatisticModel


class SensorStatisticManager:

    @staticmethod
    def get_sensor_statistics(user):
        return BaseManager.get_items(user, SensorStatisticModel)

    @staticmethod
    def create_sensor_statistic(user, data):
        data["user_id"] = user.id

        BaseManager.create_item(SensorStatisticModel, data)

    @staticmethod
    def get_sensor_statistic(user, sensor_statistic_id):
        return BaseManager.get_item(user=user, db_model=SensorStatisticModel, item_id=sensor_statistic_id, error_msg="Sensor Statistic")

    @staticmethod
    def update_sensor_statistic(user, sensor_statistic_id, data):

        BaseManager.update_item(user=user, db_model=SensorStatisticModel, item_id=sensor_statistic_id, data=data,
            error_msg="Sensor Statistic")

    @staticmethod
    def delete_sensor_statistic(user, sensor_statistic_id):
        BaseManager.delete_item(user=user, db_model=SensorStatisticModel, item_id=sensor_statistic_id, error_msg="Sensor Statistic")