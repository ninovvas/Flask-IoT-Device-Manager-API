
from db import db
from models import RoleType, UserModel
from managers.auth import AuthManager

from flask import request, jsonify

from werkzeug.exceptions import Unauthorized, NotFound
from werkzeug.security import generate_password_hash, check_password_hash


class DeviceManager:

    @staticmethod
    def login(data):
        """

        :param data:
        :return:
        """
        #user = db.session.execute(
        #    db.select(UserModel).filter_by(email=data["email"])
        #).scalar()
        user = db.session.execute(

            db.select(UserModel).filter((UserModel.username == data.get('username')) |
                                        (UserModel.email == data.get('email')))).scalar()

        if user and check_password_hash(user.password, data["password"]):
            return AuthManager.encode_token(user)
        raise Unauthorized()

    @staticmethod
    def logout(data):

        return "Successfully logged out"


    @staticmethod
    def register(data):
        """

        :param data:
        :return:
        """
        data["password"] = generate_password_hash(
            data["password"], method="pbkdf2:sha256"
        )
        data["role"] = RoleType.user.name
        user = UserModel(**data)

        db.session.add(user)
        db.session.flush()
        return AuthManager.encode_token(user)