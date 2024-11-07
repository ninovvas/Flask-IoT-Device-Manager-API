#from flask_testing import TestCase
from models import UserModel
#from models import RoleType, UserModel
from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactoryAdmin


class TestProtectedEndpoints(APIBaseTestCase):


    endpoints = (
    ("GET", "/homes"),
    ("POST", "/homes"),
    ("GET", "/homes/1"),
    ("PUT", "/homes/1"),
    ("GET", "/rooms"),
    ("POST", "/rooms"),
    ("GET", "/rooms/1"),
    ("PUT", "/rooms/1"),
    ("GET", "/sensors"),
    ("POST", "/sensors"),
    ("GET", "/sensors/1"),
    ("PUT", "/sensors/1"),
    ("GET", "/sensor_data"),
    ("POST", "/sensor_data"),
    ("GET", "/sensor_data/1"),
    ("PUT", "/sensor_data/1"),
    ("GET", "/schedules"),
    ("POST", "/schedules"),
    ("GET", "/schedules/1"),
    ("PUT", "/schedules/1"),
    ("GET", "/statistics"),
    ("POST", "/statistics"),
    ("GET", "/statistics/1"),
    ("PUT", "/statistics/1")
    )


    def make_request(self, method, url, headers=None):
        if method == "GET":
            resp = self.client.get(url, headers=headers)
        elif method == "POST":
            resp = self.client.post(url, headers=headers)
        elif method == "PUT":
            resp = self.client.put(url, headers=headers)
        else:
            resp = self.client.delete(url, headers=headers)

        return resp

    def test_login_required_endpoints_missing_token(self):
        for method, url in self.endpoints:
            resp = self.make_request(method, url)

            self.assertEqual(resp.status_code, 401)
            expected_message = {"message": "Invalid or missing token"}
            self.assertEqual(resp.json, expected_message)


    def test_login_required_endpoints_invalid_token(self):
        headers = {"Authorization": "Bearer invalid"}

        for method, url in self.endpoints:
            resp = self.make_request(method, url, headers=headers)

            self.assertEqual(resp.status_code, 401)
            expected_message = {"message": "Invalid or missing token"}
            self.assertEqual(resp.json, expected_message)

    def test_permission_required_endpoints_user(self):
        endpoints = (
            ("POST", "/homes"),
            ("GET", "/homes/1"),
            ("PUT", "/homes/1"),
            ("GET", "/rooms"),
            ("POST", "/rooms"),
            ("GET", "/rooms/1"),
            ("PUT", "/rooms/1"),
            ("GET", "/sensors"),
            ("POST", "/sensors"),
            ("GET", "/sensors/1"),
            ("PUT", "/sensors/1"),
            ("GET", "/sensor_data"),
            ("POST", "/sensor_data"),
            ("GET", "/sensor_data/1"),
            ("PUT", "/sensor_data/1"),
            ("GET", "/schedules"),
            ("POST", "/schedules"),
            ("GET", "/schedules/1"),
            ("PUT", "/schedules/1"),
            ("GET", "/statistics"),
            ("POST", "/statistics"),
            ("GET", "/statistics/1"),
            ("PUT", "/statistics/1")
        )
        user = UserFactoryAdmin()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}
        for method, url in endpoints:
            resp = self.make_request(method, url, headers=headers)

            self.assertEqual(resp.status_code, 403)
            expected_message = {
                "message": "You do not have permissions to access this resource"
            }
            self.assertEqual(resp.json, expected_message)

    # def test_permission_required_endpoints_admin(self):
    #     endpoints = (
    #         ("POST", "/users"),
    #     )
    #     user = UserFactoryAdmin()
    #     user_token = generate_token(user)
    #     headers = {"Authorization": f"Bearer {user_token}"}
    #     for method, url in endpoints:
    #         resp = self.make_request(method, url, headers=headers)
    #
    #         self.assertEqual(resp.status_code, 403)
    #         expected_message = {
    #             "message": "You do not have permissions to access this resource"
    #         }
    #         self.assertEqual(resp.json, expected_message)


class TestRegister(APIBaseTestCase):
    def test_register_schema_missing_fields(self):
        data = {}

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

        resp = self.client.post("/register", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        for field in ("email", "username", "password", "first_name", "last_name"):
            self.assertIn(field, error_message)

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

    def test_register_schema_invalid_email(self):
        data = {
            "email": "test.bg",  # This is invalid value
            "username": "test",
            "password": "testinG@1234",
            "first_name": "first_name_test",
            "last_name": "last_name_test",
            "role": "user",
        }

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

        resp = self.client.post("/register", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'email': ['Not a valid email address.']}"
        self.assertEqual(error_message, expected_message)
        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

    def test_register_schema_invalid_username(self):
        data = {
            "email": "test_1234@abv.bg",
            "username": "test@", # This is invalid value
            "password": "testinG@1234",
            "first_name": "first_name_test",
            "last_name": "last_name_test",
            "role": "user",
        }

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

        resp = self.client.post("/register", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'username': ['Username can only contain letters, numbers, dots, underscores, and hyphens.']}"
        self.assertEqual(error_message, expected_message)
        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

    def test_register_schema_invalid_password(self):
        data = {
            "email": "test_1234@abv.bg",
            "username": "test",
            "password": "testinG1234", # This is invalid value
            "first_name": "first_name_test",
            "last_name": "last_name_test",
            "role": "user",
        }

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

        resp = self.client.post("/register", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'password': ['Password must contain at least one special character.']}"
        self.assertEqual(error_message, expected_message)
        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

    def test_register_schema_invalid_role(self):
        data = {
            "email": "test_1234@abv.bg",
            "username": "test",
            "password": "testinG@1234",
            "first_name": "first_name_test",
            "last_name": "last_name_test",
            "role": "user12", # This is invalid value
        }

        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

        resp = self.client.post("/register", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'role': ['Must be one of: admin, user.']}"
        self.assertEqual(error_message, expected_message)
        users = UserModel.query.all()
        self.assertEqual(len(users), 0)

class TestLoginSchema(APIBaseTestCase):
    def test_login_schema_missing_fields(self):
        data = {}

        resp = self.client.post("/login", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'password': ['Missing data for required field.']}"
        self.assertEqual(error_message, expected_message)
        #for field in ("email", "password"):
        #    self.assertIn(field, error_message)

    def test_login_schema_invalid_email(self):

        email, password = self.register_user()

        data = {
            "email": "asd",  # This is invalid value
            "password": "testinG@1234",
        }

        self.assertNotEqual(email, data["email"])

        resp = self.client.post("/login", json=data)
        self.assertEqual(resp.status_code, 400)
        error_message = resp.json["message"]
        expected_message = "Invalid payload {'email': ['Not a valid email address.']}"
        self.assertEqual(error_message, expected_message)