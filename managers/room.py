from werkzeug.exceptions import NotFound

from db import db
from managers.base import BaseManager
from models import RoomModel, RoleType


class RoomManager:

    @staticmethod
    def get_rooms(user):
        query = db.select(RoomModel)
        query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalars().all()

    @staticmethod
    def create_room(user, data):
        data["user_id"] = user.id
        new_room = RoomModel(**data)
        db.session.add(new_room)
        db.session.flush()

    @staticmethod
    def get_room(user, room_id):
        """Get the detail information about the selected room
        :param user:
        :param room_id: the ID of the room
        :return:
        """
        return BaseManager.get_item(user=user, db_model=RoomModel, item_id=room_id, error_msg="Room")

        #query = db.select(RoomModel)
        #room = db.session.execute(
        #    query.filter_by(id=room_id)
        #).scalar()

        #if not room:
        #    raise NotFound(f"Room with id {room_id} does not exist")

        #if user.role.user == RoleType.user:
        #    query = query.filter_by(id=room_id, user_id=user.id)
        #return db.session.execute(query).scalar()

    @staticmethod
    def update_room(user, room_id, data):

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
        home = db.session.execute(
            db.select(RoomModel).filter_by(id=room_id, user_id=user.id)
        ).scalar()
        if not home:
            raise NotFound(f"Room with id {room_id} does not exist")

        db.session.delete(home)
        db.session.flush()
