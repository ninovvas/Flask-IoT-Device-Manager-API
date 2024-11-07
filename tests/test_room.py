from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory, RoomFactory


class TestRoomResource(APIBaseTestCase):
    def test_create_room(self):

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # create Home
        home = HomeFactory(user_id=user.id)

        # Create Room

        data = {
            "name": "Test Room",
            "description": "A room for testing purposes.",
            "home_id": home.id,
        }

        response = self.client.post(
            "/rooms",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Room created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_get_one_room(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)

        response = self.client.get(f"/rooms/{room.id}", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["room"]["id"], room.id)

    def test_get_all_rooms(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        RoomFactory.create_batch(1, user_id=user.id, home_id=home.id)

        response = self.client.get("/rooms", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_edit_room(self):

        user = UserFactory()
        print(f"#####################")
        print(f"user ID {user.id}")
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # create Home
        home = HomeFactory(user_id=user.id)

        # Create a room to edit
        room = RoomFactory(user_id=user.id, home_id=home.id)

        # Edit the room
        edit_data = {
            "name": "Updated Room",
            "description": "Updated description.",
            "home_id": 1,
        }
        response_edit = self.client.put(
            f"/rooms/{room.id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Room updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_room(self):

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # create Home
        home = HomeFactory(user_id=user.id)

        # Create a room to edit
        room = RoomFactory(user_id=user.id, home_id=home.id)

        # Delete the room
        response = self.client.delete(f"/rooms/{room.id}", headers=headers)
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(f"/rooms/1", headers=headers)
        self.assertEqual(get_response.status_code, 404)
