from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory


class TestRoomResource(APIBaseTestCase):
    def test_create_room(self):

        # Create home

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

        # Create Room

        data = {
            "name": "Test Room",
            "description": "A room for testing purposes.",
            "home_id": 1
        }

        #user = UserFactory()
        #user_token = generate_token(user)
        #headers = {"Authorization": f"Bearer {user_token}"}
        response = self.client.post(
            "/rooms",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Room created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_edit_room(self):
        # Create home

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

        # Create a room to edit
        create_data = {
            "name": "Initial Room",
            "description": "Initial description.",
            "home_id": 1
        }

        create_response = self.client.post(
            "/rooms",
            headers=headers,
            json=create_data,
        )

        self.assertEqual(create_response.status_code, 201)
        expected_message = {"message": "Room created successfully"}
        self.assertEqual(create_response.json, expected_message)

        # Edit the room
        edit_data = {
            "name": "Updated Room",
            "description": "Updated description.",
            "home_id": 1
        }
        response_edit = self.client.put(
            f"/rooms/1",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Room updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_room(self):
        # Create home

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

        # Create a room to delete
        create_data = {
            "name": "Room to Delete",
            "description": "This room will be deleted.",
            "home_id": 1
        }

        create_response = self.client.post(
            "/rooms",
            headers=headers,
            json=create_data,
        )


        # Delete the room
        response = self.client.delete(
            f"/rooms/1",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/rooms/1",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)
