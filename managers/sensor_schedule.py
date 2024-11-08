from managers.base import BaseManager
from models import SensorScheduleModel


class SensorScheduleManager:

    @staticmethod
    def get_sensor_schedules(user):
        """
        Get all sensor schedules associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of sensor schedules belonging to the user.
        :rtype: list
        """
        return BaseManager.get_items(user, SensorScheduleModel)

    @staticmethod
    def create_sensor_schedule(user, data):
        """
        Create a new sensor schedule associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the sensor schedule details.
        :type data: dict
        :return: The newly created sensor schedule instance.
        :rtype: SensorScheduleModel
        """
        data["user_id"] = user.id

        BaseManager.create_item(SensorScheduleModel, data)

    @staticmethod
    def get_sensor_schedule(user, sensor_schedule_id):
        """
        Retrieve a specific sensor schedule by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_schedule_id: The ID of the sensor schedule to retrieve.
        :type sensor_schedule_id: int
        :return: The sensor schedule instance if it exists and belongs to the user.
        :rtype: SensorScheduleModel
        :raises NotFound: If the sensor schedule with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user,
            db_model=SensorScheduleModel,
            item_id=sensor_schedule_id,
            error_msg="Sensor Schedule",
        )

    @staticmethod
    def update_sensor_schedule(user, sensor_schedule_id, data):
        """
        Update an existing sensor schedule for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_schedule_id: The ID of the sensor schedule to update.
        :type sensor_schedule_id: int
        :param data: A dictionary containing the updated sensor schedule details.
        :type data: dict
        :raises NotFound: If the sensor schedule with the given ID does not exist or does not belong to the user.
        """
        BaseManager.update_item(
            user=user,
            db_model=SensorScheduleModel,
            item_id=sensor_schedule_id,
            data=data,
            error_msg="Sensor Schedule",
        )

    @staticmethod
    def delete_sensor_schedule(user, sensor_schedule_id):
        """
        Delete a sensor schedule associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_schedule_id: The ID of the sensor schedule to delete.
        :type sensor_schedule_id: int
        :raises NotFound: If the sensor schedule with the given ID does not exist or does not belong to the user.
        """
        BaseManager.delete_item(
            user=user,
            db_model=SensorScheduleModel,
            item_id=sensor_schedule_id,
            error_msg="Sensor Schedule",
        )
