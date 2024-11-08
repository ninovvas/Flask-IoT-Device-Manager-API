from werkzeug.exceptions import Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import RoleType, UserModel


class DeviceManager:

    @staticmethod
    def login(data):
        """
        Authenticate a user based on provided credentials.

        :param data: A dictionary containing login credentials, such as "username" and/or "email", and "password".
        :type data: dict
        :return: A JSON Web Token (JWT) if the authentication is successful.
        :rtype: str
        :raises Unauthorized: If the credentials are invalid.
        """
        user = db.session.execute(
            db.select(UserModel).filter(
                (UserModel.username == data.get("username"))
                | (UserModel.email == data.get("email"))
            )
        ).scalar()

        if user and check_password_hash(user.password, data["password"]):
            return AuthManager.encode_token(user)
        raise Unauthorized()

    @staticmethod
    def logout(data):

        return "Successfully logged out"

    @staticmethod
    def register(data):
        """
        Register a new user in the system.

        :param data: A dictionary containing user registration details, such as "username", "email", and "password".
        :type data: dict
        :return: A JSON Web Token (JWT) for the newly registered user.
        :rtype: str
        """
        data["password"] = generate_password_hash(
            data["password"], method="pbkdf2:sha256"
        )
        data["role"] = RoleType.user.name
        user = UserModel(**data)

        db.session.add(user)
        db.session.flush()
        return AuthManager.encode_token(user)
