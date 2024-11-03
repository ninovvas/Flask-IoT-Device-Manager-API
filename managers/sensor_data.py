from werkzeug.exceptions import NotFound

from managers.base import BaseManager
from models import SensorDataModel


class SensorDataManager:

    @staticmethod
    def get_sensor_datas(user):
        return BaseManager.get_items(user,SensorDataModel)

    @staticmethod
    def create_sensor_data(user, data):
        data["user_id"] = user.id

        BaseManager.create_item(SensorDataModel, data)

    @staticmethod
    def get_sensor_data(user, sensor_data_id):
        return BaseManager.get_item(user=user, db_model=SensorDataModel, item_id=sensor_data_id, error_msg="Sensor Data")

    @staticmethod
    def update_sensor_data(user, sensor_data_id, data):

        BaseManager.update_item(user=user, db_model=SensorDataModel, item_id=sensor_data_id, data=data,
            error_msg="Sensor Data")

    @staticmethod
    def delete_sensor_data(user, sensor_data_id):
        BaseManager.delete_item(user=user, db_model=SensorDataModel, item_id=sensor_data_id, error_msg="Sensor Data")