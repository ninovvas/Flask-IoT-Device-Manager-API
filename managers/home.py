from werkzeug.exceptions import NotFound

from db import db
from managers.base import BaseManager
from models import HomeModel, RoleType


class HomeManager:

    @staticmethod
    def get_homes(user):
        """
        Get all homes associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of homes belonging to the user.
        :rtype: list
        """
        query = db.select(HomeModel)
        if user.role.user == RoleType.user:
            query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalars().all()

    @staticmethod
    def create_home(user, data):
        """
        Create a new home associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param data: A dictionary containing the home details.
        :type data: dict
        :return: The newly created home instance.
        :rtype: HomeModel
        """
        data["user_id"] = user.id
        new_home = HomeModel(**data)
        db.session.add(new_home)
        db.session.flush()

    @staticmethod
    def get_home(user, home_id):
        """
        Retrieve a specific home by ID for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param home_id: The ID of the home to retrieve.
        :type home_id: int
        :return: The home instance if it exists and belongs to the user.
        :rtype: HomeModel
        :raises NotFound: If the home with the given ID does not exist.
        """
        return BaseManager.get_item(
            user=user, db_model=HomeModel, item_id=home_id, error_msg="Home"
        )

    @staticmethod
    def update_home(user, home_id, data):
        """
        Update an existing home for the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param home_id: The ID of the home to update.
        :type home_id: int
        :param data: A dictionary containing the updated home details.
        :type data: dict
        :raises NotFound: If the home with the given ID does not exist or does not belong to the user.
        """

        home = db.session.execute(
            db.select(HomeModel).filter_by(id=home_id, user_id=user.id)
        ).scalar()

        if not home:
            raise NotFound(f"Home with id {home_id} does not exist!")

        for key, value in data.items():
            setattr(home, key, value)

        db.session.flush()

    @staticmethod
    def delete_home(user, home_id):
        """
        Delete a home associated with the given user.

        :param user: User object representing the current user.
        :type user: UserModel
        :param home_id: The ID of the home to delete.
        :type home_id: int
        :raises NotFound: If the home with the given ID does not exist or does not belong to the user.
        """
        home = db.session.execute(
            db.select(HomeModel).filter_by(id=home_id, user_id=user.id)
        ).scalar()
        if not home:
            raise NotFound(f"Home with id {home_id} does not exist")

        db.session.delete(home)
        db.session.flush()
