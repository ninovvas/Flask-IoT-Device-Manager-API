from werkzeug.exceptions import NotFound

from db import db
from managers.base import BaseManager
from models import HomeModel, RoleType


class HomeManager:

    def get_homes(user):
        query = db.select(HomeModel)
        if user.role.user == RoleType.user:
            query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalars().all()

    def create_home(user, data):
        data["user_id"] = user.id
        new_home = HomeModel(**data)
        db.session.add(new_home)
        db.session.flush()

    def get_home(user, home_id):

        return BaseManager.get_item(user=user, db_model=HomeModel, item_id=home_id, error_msg="Home")

    def update_home(user, home_id, data):

        home = db.session.execute(
            db.select(HomeModel).filter_by(id=home_id, user_id=user.id)
        ).scalar()

        if not home:
            raise NotFound(f"Home with id {home_id} does not exist!")

        for key, value in data.items():
            setattr(home, key, value)

        db.session.flush()

    def delete_home(user, home_id):
        home = db.session.execute(
            db.select(HomeModel).filter_by(id=home_id, user_id=user.id)
        ).scalar()
        if not home:
            raise NotFound(f"Home with id {home_id} does not exist")

        db.session.delete(home)
        db.session.flush()
