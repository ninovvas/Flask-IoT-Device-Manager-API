from werkzeug.exceptions import NotFound

from db import db
from models import RoleType


class BaseManager:

    @staticmethod
    def get_items(user, db_model):
        """

        :param user:
        :param db_model:
        :return:
        """
        query = db.select(db_model)
        query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalars().all()

    @staticmethod
    def get_item(user, db_model, item_id, error_msg):
        """

        :param user:
        :param db_model:
        :param item_id:
        :param error_msg:
        :return:
        """

        query = db.select(db_model)
        item = db.session.execute(query.filter_by(id=item_id)).scalar()

        if not item:
            raise NotFound(f"{error_msg} with id {item_id} does not exist")

        if user.role.user == RoleType.user:
            query = query.filter_by(id=item_id, user_id=user.id)

        return db.session.execute(query).scalar()

    @staticmethod
    def create_item(db_model, data):
        """Creates a new item in the database.
        :param db_model: The database model class to create an instance of.
                         This model should map to a table in the database.
        :param data: A dictionary containing the data for the new item.
                     The keys should match the fields of the db_model.
        :return: The newly created item instance with its ID generated by the database.
        """

        new_item = db_model(**data)
        db.session.add(new_item)
        db.session.flush()

    @staticmethod
    def update_item(user, db_model, item_id, data, error_msg):
        item = db.session.execute(
            db.select(db_model).filter_by(id=item_id, user_id=user.id)
        ).scalar()

        if not item:
            raise NotFound(f"{error_msg} with id {item} does not exist!")

        for key, value in data.items():
            setattr(item, key, value)

        db.session.flush()

    @staticmethod
    def delete_item(user, db_model, item_id, error_msg):
        """
        :param user:
        :param db_model:
        :param item_id:
        :param error_msg:
        :return:
        """
        home = db.session.execute(
            db.select(db_model).filter_by(id=item_id, user_id=user.id)
        ).scalar()
        if not home:
            raise NotFound(f"{error_msg} with id {item_id} does not exist")

        db.session.delete(home)
        db.session.flush()

    @staticmethod
    def check_item_exists(user, db_model, item_id):
        item = db.session.execute(
            db.select(db_model).filter_by(id=item_id, user_id=user.id)
        ).scalar()
        return item
