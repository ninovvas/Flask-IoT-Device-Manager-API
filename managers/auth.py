from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import Unauthorized

from db import db
from models.user import UserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        """
        Generate a JSON Web Token (JWT) for the given user.

        :param user: User object containing user details like `id` and `role`.
        :type user: UserModel
        :return: Encoded JWT as a string.
        :rtype: str
        """

        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=2),
            "role": user.role if isinstance(user.role, str) else user.role.name,
        }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        """
        Decode a JSON Web Token (JWT) to retrieve the user ID and role.

        :param token: The JWT to be decoded.
        :type token: str
        :return: A tuple containing the user ID and role.
        :rtype: tuple(int, str)
        :raises jwt.ExpiredSignatureError: If the token has expired.
        :raises jwt.InvalidTokenError: If the token is invalid.
        """
        try:
            info = jwt.decode(jwt=token, key=config("SECRET_KEY"), algorithms=["HS256"])
            return info["sub"], info["role"]
        except Exception as ex:
            raise ex


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    """
    Verify the given token and retrieve the corresponding user from the database.

    :param token: The JWT to be verified.
    :type token: str
    :return: User object if the token is valid.
    :rtype: UserModel
    :raises Unauthorized: If the token is invalid or missing.
    """
    try:
        user_id, type_user = AuthManager.decode_token(token)
        return db.session.execute(db.select(UserModel).filter_by(id=user_id)).scalar()
    except Exception:
        raise Unauthorized("Invalid or missing token")
