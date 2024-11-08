from models import RoleType, UserModel
from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory


class TestCreateUser(APIBaseTestCase):
    def test_permission_required_only_admins_allowed(self):
        user = UserFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.client.post("/admins/users", headers=headers)

        self.assertEqual(resp.status_code, 403)
        self.assertEqual(
            resp.json,
            {"message": "You do not have permissions to access this resource"},
        )

    def test_register_user(self):
        user = UserFactory(id=0, role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "username": "User_form_Admin",
            "password": "parolkA@123",
            "first_name": "User form Admin1",
            "last_name": "ser form Admin2",
            "email": "auser10@abv.bg",
            "role": RoleType.admin.value,
        }

        users = UserModel.query.all()
        self.assertEqual(len(users), 1)

        resp = self.client.post("/admins/users", headers=headers, json=data)

        self.assertEqual(resp.status_code, 201)
        users = UserModel.query.all()
        self.assertEqual(len(users), 2)

        new_user = UserModel.query.filter_by(username=data["username"]).all()
        self.assertEqual(len(new_user), 1)
        self.assertEqual(new_user[0].role, RoleType.admin)
