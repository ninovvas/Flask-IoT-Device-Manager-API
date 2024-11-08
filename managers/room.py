from werkzeug.exceptions import NotFound

from db import db
from managers.base import BaseManager
from models import RoomModel


class RoomManager:

    @staticmethod
    def get_rooms(user):
        """
        Get all rooms associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of rooms belonging to the user.
        :rtype: list
        """
        query = db.select(RoomModel)
        query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalars().all()

    @staticmethod
    def create_room(user, data):
        """
        Create a new room associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the room details.
        :type data: dict
        :return: The newly created room instance.
        :rtype: RoomModel
        """
        data["user_id"] = user.id
        new_room = RoomModel(**data)
        db.session.add(new_room)
        db.session.flush()

    @staticmethod
    def get_room(user, room_id):
        """
        Retrieve a specific room by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param room_id: The ID of the room to retrieve.
        :type room_id: int
        :return: The room instance if it exists and belongs to the user.
        :rtype: RoomModel
        :raises NotFound: If the room with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user, db_model=RoomModel, item_id=room_id, error_msg="Room"
        )

    @staticmethod
    def update_room(user, room_id, data):
        """
        Update an existing room for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param room_id: The ID of the room to update.
        :type room_id: int
        :param data: A dictionary containing the updated room details.
        :type data: dict
        :raises NotFound: If the room with the given ID does not exist or does not belong to the user.
        """
        room = db.session.execute(
            db.select(RoomModel).filter_by(id=room_id, user_id=user.id)
        ).scalar()

        if not room:
            raise NotFound(f"Room with id {room_id} does not exist!")

        for key, value in data.items():
            setattr(room, key, value)

        db.session.flush()

    @staticmethod
    def delete_room(user, room_id):
        """
        Delete a room associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param room_id: The ID of the room to delete.
        :type room_id: int
        :raises NotFound: If the room with the given ID does not exist or does not belong to the user.
        """
        home = db.session.execute(
            db.select(RoomModel).filter_by(id=room_id, user_id=user.id)
        ).scalar()
        if not home:
            raise NotFound(f"Room with id {room_id} does not exist")

        db.session.delete(home)
        db.session.flush()
