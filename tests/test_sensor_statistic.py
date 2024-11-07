from datetime import datetime, timedelta

from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory, RoomFactory, SensorFactory, SensorStatisticFactory

class TestSensorStatisticResource(APIBaseTestCase):
    def test_create_sensor_statistic(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, and Sensor
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        # Sensor statistic data
        data = {
            "sensor_id": sensor.id,
            "average_value": 30.0,
            "min_value": 10.0,
            "max_value": 50.0,
        }

        response = self.client.post(
            "/statistics",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Sensor Statistic created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_get_one_sensor_statistic(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_statistic = SensorStatisticFactory(sensor_id=sensor.id, user_id=user.id)

        response = self.client.get(f"/statistics/{sensor_statistic.id}", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["sensor_statistic"]["id"], sensor_statistic.id)

    def test_get_all_sensor_statistics(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        SensorStatisticFactory.create_batch(1, sensor_id=sensor.id, user_id=user.id)

        response = self.client.get("/statistics", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_edit_sensor_statistic(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Statistic
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_statistic = SensorStatisticFactory(sensor_id=sensor.id, user_id=user.id)

        # Edit the sensor statistic
        edit_data = {
            "sensor_id": sensor.id,
            "average_value": 30.0,
            "min_value": 10.0,
            "max_value": 50.0
        }

        response_edit = self.client.put(
            f"/statistics/{sensor_statistic.id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Sensor Statistic updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_sensor_statistic(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Statistic
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_statistic = SensorStatisticFactory(sensor_id=sensor.id, user_id=user.id)

        # Delete the sensor statistic
        response = self.client.delete(
            f"/statistics/{sensor_statistic.id}",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/statistics/{sensor_statistic.id}",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)
