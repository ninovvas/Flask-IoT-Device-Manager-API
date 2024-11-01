from flask import request
from flask_restful import Resource

#from managers.auth import auth
from managers.device_manager import DeviceManager



class RegisterUser(Resource):
    #@validate_schema(UserRegisterSchema)
    def post(self):
        data = request.get_json()
        token = DeviceManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    #@validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        token = DeviceManager.login(data)
        return {"token": token}