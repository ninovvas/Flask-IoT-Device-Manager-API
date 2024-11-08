from managers.base import BaseManager
from models import SensorStatisticModel


class SensorStatisticManager:

    @staticmethod
    def get_sensor_statistics(user):
        """
        Get all sensor statistics associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of sensor statistics belonging to the user.
        :rtype: list
        """
        return BaseManager.get_items(user, SensorStatisticModel)

    @staticmethod
    def create_sensor_statistic(user, data):
        """
        Create a new sensor statistic associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the sensor statistic details.
        :type data: dict
        :return: The newly created sensor statistic instance.
        :rtype: SensorStatisticModel
        """
        data["user_id"] = user.id

        BaseManager.create_item(SensorStatisticModel, data)

    @staticmethod
    def get_sensor_statistic(user, sensor_statistic_id):
        """
        Retrieve a specific sensor statistic by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_statistic_id: The ID of the sensor statistic to retrieve.
        :type sensor_statistic_id: int
        :return: The sensor statistic instance if it exists and belongs to the user.
        :rtype: SensorStatisticModel
        :raises NotFound: If the sensor statistic with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user,
            db_model=SensorStatisticModel,
            item_id=sensor_statistic_id,
            error_msg="Sensor Statistic",
        )

    @staticmethod
    def update_sensor_statistic(user, sensor_statistic_id, data):
        """
        Update an existing sensor statistic for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_statistic_id: The ID of the sensor statistic to update.
        :type sensor_statistic_id: int
        :param data: A dictionary containing the updated sensor statistic details.
        :type data: dict
        :raises NotFound: If the sensor statistic with the given ID does not exist or does not belong to the user.
        """

        BaseManager.update_item(
            user=user,
            db_model=SensorStatisticModel,
            item_id=sensor_statistic_id,
            data=data,
            error_msg="Sensor Statistic",
        )

    @staticmethod
    def delete_sensor_statistic(user, sensor_statistic_id):
        """
        Delete a sensor statistic associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_statistic_id: The ID of the sensor statistic to delete.
        :type sensor_statistic_id: int
        :raises NotFound: If the sensor statistic with the given ID does not exist or does not belong to the user.
        """
        BaseManager.delete_item(
            user=user,
            db_model=SensorStatisticModel,
            item_id=sensor_statistic_id,
            error_msg="Sensor Statistic",
        )
