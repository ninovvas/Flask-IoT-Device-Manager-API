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
        """
        Get all sensor data records associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of sensor data records belonging to the user.
        :rtype: list
        """
        return BaseManager.get_items(user, SensorDataModel)

    @staticmethod
    def create_sensor_data(user, data):
        """
        Create a new sensor data record and optionally notify via email if the threshold is exceeded.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the sensor data details.
        :type data: dict
        :raises NotFound: If the sensor with the given ID does not exist.
        """

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
        """
        Retrieve a specific sensor data record by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_data_id: The ID of the sensor data record to retrieve.
        :type sensor_data_id: int
        :return: The sensor data instance if it exists and belongs to the user.
        :rtype: SensorDataModel
        :raises NotFound: If the sensor data with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            error_msg="Sensor Data",
        )

    @staticmethod
    def update_sensor_data(user, sensor_data_id, data):
        """
        Update an existing sensor data record for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_data_id: The ID of the sensor data record to update.
        :type sensor_data_id: int
        :param data: A dictionary containing the updated sensor data details.
        :type data: dict
        :raises NotFound: If the sensor data with the given ID does not exist or does not belong to the user.
        """
        BaseManager.update_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            data=data,
            error_msg="Sensor Data",
        )

    @staticmethod
    def delete_sensor_data(user, sensor_data_id):
        """
        Delete a sensor data record associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_data_id: The ID of the sensor data record to delete.
        :type sensor_data_id: int
        :raises NotFound: If the sensor data with the given ID does not exist or does not belong to the user.
        """
        BaseManager.delete_item(
            user=user,
            db_model=SensorDataModel,
            item_id=sensor_data_id,
            error_msg="Sensor Data",
        )
