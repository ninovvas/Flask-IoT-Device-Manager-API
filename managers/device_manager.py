
from werkzeug.exceptions import Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import RoleType, UserModel


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


    #def get_homes(user):
    #    query = db.select(HomeModel)
    #    if user.role.user == RoleType.user:
    #        query = query.filter_by(user_id=user.id)
    #    return db.session.execute(query).scalar().all()

    #def create_home(user, data):
    #    data["user_id"] = user.id
    #    new_home = HomeModel(**data)
    #    db.session.add(new_home)
    #    db.session.flush()
    #    db.session.commit()
    #    db.session.commit()