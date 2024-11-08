from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import auth
from models import UserModel, RoleType


class UserManager:
    @staticmethod
    def create_user(user_data):
        """
        Create a new user with the provided data.

        :param user_data: A dictionary containing the user details such as username, email, and password.
        :type user_data: dict
        :return: The newly created user instance.
        :rtype: UserModel
        """
        user_data["password"] = generate_password_hash(
            user_data["password"], method="pbkdf2:sha256"
        )
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.flush()

    @staticmethod
    def change_password(pass_data):
        """
        Change the password for the current user.

        :param pass_data: A dictionary containing the old and new passwords.
        :type pass_data: dict
        :raises BadRequest: If the old password is incorrect.
        """
        user = auth.current_user()

        if not check_password_hash(user.password, pass_data["old_password"]):
            raise BadRequest("Invalid password")

        user.password = generate_password_hash(
            pass_data["new_password"], method="pbkdf2:sha256"
        )
        db.session.add(user)
        db.session.flush()

    @staticmethod
    def get_users(user):
        """
        Retrieve all users if the current user is an admin.

        :param user: User object representing the current user.
        :type user: UserModel
        :return: A list of all users if the user is an admin.
        :rtype: list
        :raises BadRequest: If the current user is not an admin.
        """
        if user.role.admin == RoleType.admin:
            query = db.select(UserModel)
            return db.session.execute(query).scalars().all()
        else:
            raise BadRequest("The user is not admin!")
