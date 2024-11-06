import factory
from werkzeug.security import generate_password_hash

from db import db
from models import UserModel, RoleType


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
