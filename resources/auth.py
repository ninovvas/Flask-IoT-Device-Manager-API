from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.exceptions import Unauthorized

from managers.auth import auth
from managers.device_manager import DeviceManager
from models import UserModel
from schemas.request.user import UserRegisterSchema, UserLoginSchema
from util.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        data = request.get_json()

        try:
            user_data = UserRegisterSchema().load(data)
        except ValidationError as err:
            return err.messages, 400

            # Check if email or username already exists
        if UserModel.query.filter_by(email=user_data["email"]).first():
            return {"message": "Email already exists"}, 400
        if UserModel.query.filter_by(username=user_data["username"]).first():
            return {"message": "Username already exists"}, 400

        token = DeviceManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        token = DeviceManager.login(data)
        return {"token": token}


# Logout endpoint
class LogoutUser(Resource):
    @auth.login_required
    def post(self):
        data = request.get_json()
        # Get the token from the request
        token = data.get("token")

        # If no token is provided, raise an error
        if not token:
            raise Unauthorized("Token is required for logout")

        response = DeviceManager.logout(data)
        return {"message": response}, 200
