
from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory


class TestHomeResource(APIBaseTestCase):


    def test_create_home(self):
        # Test the creation of a new home with correct parameters

        data = {
            "address": "123 Test St",
            "city": "Testville",
            "state": "TS",
            "zip_code": "12345"
        }

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}
        response = self.client.post(
            "/homes",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Home created successfully"}
        self.assertEqual(response.json, expected_message)

        # Home tests

    def test_get_one_home(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)

        response = self.client.get(f"/homes/{home.id}", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['home']['id'], home.id)

    def test_get_all_homes(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}


        HomeFactory(user_id=user.id)

        response = self.client.get("/homes", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_edit_home(self):
        # First, create a home to edit
        create_data = {
            "address": "456 Initial Ave",
            "city": "Initial City",
            "state": "IC",
            "zip_code": "67890"
        }
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}
        create_response = self.client.post(
            "/homes",
            headers=headers,
            json=create_data,
        )
        expected_message = {"message": "Home created successfully"}
        self.assertEqual(create_response.json, expected_message)
        home_id = 1

        # Edit the home
        edit_data = {
            "address": "789 Updated Blvd",
            "city": "Updated City",
            "state": "UC",
            "zip_code": "98765"
        }
        response = self.client.put(
            f"/homes/{home_id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response.status_code, 200)
        expected_message = {"message": "Home updated successfully"}
        self.assertEqual(response.json, expected_message)

    def test_delete_home(self):
        # First, create a home to delete
        create_data = {
            "address": "Home to Delete St",
            "city": "Delete City",
            "state": "DC",
            "zip_code": "11111"
        }
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}
        create_response = self.client.post(
            "/homes",
            headers=headers,
            json=create_data,
        )
        expected_message = {"message": "Home created successfully"}
        self.assertEqual(create_response.json, expected_message)
        home_id = 1

        # Delete the home
        response = self.client.delete(
            f"/homes/{home_id}",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/homes/{home_id}",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)

