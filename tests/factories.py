import factory
from werkzeug.security import generate_password_hash

from db import db
from models import UserModel, RoleType, HomeModel, RoomModel, SensorModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        if hasattr(object, "password:"):
            plain_pass = object.password
            object.password = generate_password_hash(plain_pass, method="pbkdf2:sha256")
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    username = "username"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.user

class UserFactoryAdmin(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    username = "admin"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.admin


class UserFactoryAdmin(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    username = "admin"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.admin


class HomeFactory(BaseFactory):
    class Meta:
        model = HomeModel

    address = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zip_code =  factory.Sequence(lambda n: 70000 + n)
    user_id = factory.SubFactory(UserFactory)

class RoomFactory(BaseFactory):
    class Meta:
        model = RoomModel

    name = factory.Faker("name")
    description = "Tis is a new room"
    home_id = factory.SubFactory(HomeFactory)
    user_id = factory.SubFactory(UserFactory)

class SensorFactory(BaseFactory):
    class Meta:
        model = SensorModel

    name = factory.Faker("name")
    sensor_type = "Sensor_Tst_Type"
    producer = "Bosh"
    interface = "CAN"
    room_id = factory.SubFactory(RoomFactory)
    user_id = factory.SubFactory(UserFactory)
