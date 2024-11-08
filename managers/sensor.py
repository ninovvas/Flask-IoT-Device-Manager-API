from werkzeug.exceptions import NotFound

from managers.base import BaseManager
from models import RoomModel, SensorModel


class SensorManager:

    @staticmethod
    def get_sensors(user):
        """
        Get all sensors associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of sensors belonging to the user.
        :rtype: list
        """
        return BaseManager.get_items(user, SensorModel)

    @staticmethod
    def create_sensor(user, data):
        """
        Create a new sensor associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the sensor details.
        :type data: dict
        :raises NotFound: If the room with the given room ID does not exist.
        """
        data["user_id"] = user.id
        room_id = data.get("room_id")

        if room_id:
            room = BaseManager.check_item_exists(
                user=user, db_model=RoomModel, item_id=room_id
            )
            if not room:
                raise NotFound(f"Room with id {room_id} does not exist!")

        BaseManager.create_item(SensorModel, data)

    @staticmethod
    def get_sensor(user, sensor_id):
        """
        Retrieve a specific sensor by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_id: The ID of the sensor to retrieve.
        :type sensor_id: int
        :return: The sensor instance if it exists and belongs to the user.
        :rtype: SensorModel
        :raises NotFound: If the sensor with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user, db_model=SensorModel, item_id=sensor_id, error_msg="Sensor"
        )

    @staticmethod
    def update_sensor(user, sensor_id, data):
        """
        Update an existing sensor for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_id: The ID of the sensor to update.
        :type sensor_id: int
        :param data: A dictionary containing the updated sensor details.
        :type data: dict
        :raises NotFound: If the sensor or the room with the given ID does not exist.
        """
        room_id = data.get("room_id")

        if room_id:
            room = BaseManager.check_item_exists(
                user=user, db_model=RoomModel, item_id=room_id
            )
            if not room:
                raise NotFound(f"Room with id {room_id} does not exist!")

        BaseManager.update_item(
            user=user,
            db_model=SensorModel,
            item_id=sensor_id,
            data=data,
            error_msg="Sensor",
        )

    @staticmethod
    def delete_sensor(user, sensor_id):
        """
        Delete a sensor associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param sensor_id: The ID of the sensor to delete.
        :type sensor_id: int
        :raises NotFound: If the sensor with the given ID does not exist or does not belong to the user.
        """
        BaseManager.delete_item(
            user=user, db_model=SensorModel, item_id=sensor_id, error_msg="Sensor"
        )
