from werkzeug.exceptions import NotFound

from managers.base import BaseManager
from models import RoomModel, SensorModel


class SensorManager:

    @staticmethod
    def get_sensors(user):
        return BaseManager.get_items(user,SensorModel)

    @staticmethod
    def create_sensor(user, data):
        data["user_id"] = user.id
        room_id = data.get("room_id")

        if room_id:
            room = BaseManager.check_item_exists(user=user, db_model=RoomModel, item_id=room_id)
            if not room:
                raise NotFound(f"Room with id {room_id} does not exist!")

        BaseManager.create_item(SensorModel, data)

    @staticmethod
    def get_sensor(user, sensor_id):
        return BaseManager.get_item(user=user, db_model=SensorModel, item_id=sensor_id, error_msg="Sensor")

    @staticmethod
    def update_sensor(user, sensor_id, data):

        room_id = data.get("room_id")

        if room_id:
            room = BaseManager.check_item_exists(user=user, db_model=RoomModel, item_id=room_id)
            if not room:
                raise NotFound(f"Room with id {room_id} does not exist!")

        BaseManager.update_item(user=user, db_model=SensorModel, item_id=sensor_id, data=data,
            error_msg="Sensor")

    @staticmethod
    def delete_sensor(user, sensor_id):
        BaseManager.delete_item(user=user, db_model=SensorModel, item_id=sensor_id, error_msg="Sensor")