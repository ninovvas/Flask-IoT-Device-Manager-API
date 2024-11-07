from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory, RoomFactory, SensorFactory

class TestSensorResource(APIBaseTestCase):
    def test_create_sensor(self):

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home and Room
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)

        # Sensor data
        data = {
            "name": "Temperature Sensor",
            "sensor_type": "temperature",
            "producer": "Siemens",
            "interface": "I2C",
            "room_id": room.id
        }

        response = self.client.post(
            "/sensors",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Sensor created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_get_one_sensor(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        response = self.client.get(f"/sensors/{sensor.id}", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["sensor"]["id"], sensor.id)

    def test_get_all_sensors(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        SensorFactory.create_batch(1, user_id=user.id, room_id=room.id)

        response = self.client.get("/sensors", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_edit_sensor(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, and Sensor
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        # Edit the sensor
        edit_data = {
            "name": "Temperature Sensor",
            "sensor_type": "temperature",
            "producer": "Siemens",
            "interface": "I2C",
            "room_id": room.id
        }
        response_edit = self.client.put(
            f"/sensors/{sensor.id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Sensor updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_sensor(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, and Sensor
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        # Delete the sensor
        response = self.client.delete(
            f"/sensors/{sensor.id}",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/sensors/{sensor.id}",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)
