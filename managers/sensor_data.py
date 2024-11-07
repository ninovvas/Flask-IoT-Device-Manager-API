from decouple import config

from managers.base import BaseManager
from models import SensorDataModel, SensorModel
from services.maileroo import MailerooService
from services.sendgrid import SendGridService

grid_service = SendGridService()
maileroo_service = MailerooService()
NOTIFY_VALUE = 50


class SensorDataManager:

    @staticmethod
    def get_sensor_datas(user):
        return BaseManager.get_items(user, SensorDataModel)

    @staticmethod
    def create_sensor_data(user, data):

        data["user_id"] = user.id

        email_data = {}
        # get sensor name for the name
        email_data["value"] = data.get("value")
        sensor_id = data.get("sensor_id")
        sensor = BaseManager.check_item_exists(user, SensorModel, sensor_id)
        email_data["sensor_name"] = sensor.name

        if config("ENABLE_SENDGRID") == "True":
            # Send email if the sensor value is bigger or equal to NOTIFY_VALUE
            grid_service.notify_sensor_data_threshold(email_data, NOTIFY_VALUE)
        if config("ENABLE_MAILEROO_SERVICE") == "True":
            maileroo_service.notify_sensor_data_threshold(email_data, NOTIFY_VALUE)

        BaseManager.create_item(SensorDataModel, data)

    @staticmethod
    def get_sensor_data(user, sensor_data_id):
        return BaseManager.get_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            error_msg="Sensor Data",
        )

    @staticmethod
    def update_sensor_data(user, sensor_data_id, data):

        BaseManager.update_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            data=data,
            error_msg="Sensor Data",
        )

    @staticmethod
    def delete_sensor_data(user, sensor_data_id):
        BaseManager.delete_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            error_msg="Sensor Data",
        )
