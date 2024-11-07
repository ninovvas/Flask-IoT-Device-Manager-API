from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory, RoomFactory, SensorFactory, SensorDataFactory

class TestSensorDataResource(APIBaseTestCase):
    def test_create_sensor_data(self):

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, and Sensor
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        # Sensor data entry
        data = {
            "sensor_id": sensor.id,
            "value": 23.5
        }

        response = self.client.post(
            "/sensor_data",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Sensor Data created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_edit_sensor_data(self):

        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Data
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_data = SensorDataFactory(sensor_id=sensor.id, user_id=user.id)

        # Edit the sensor data
        edit_data = {
            "sensor_id": sensor.id,
            "value": 30.0
        }
        response_edit = self.client.put(
            f"/sensor_data/{sensor_data.id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Sensor Data updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_sensor_data(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Data
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_data = SensorDataFactory(sensor_id=sensor.id, user_id=user.id)

        # Delete the sensor data
        response = self.client.delete(
            f"/sensor_data/{sensor_data.id}",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/sensor_data/{sensor_data.id}",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)
