from datetime import datetime, timedelta

from tests.base import APIBaseTestCase, generate_token
from tests.factories import UserFactory, HomeFactory, RoomFactory, SensorFactory, SensorScheduleFactory

class TestSensorScheduleResource(APIBaseTestCase):
    def test_create_sensor_schedule(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, and Sensor
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)

        # Sensor schedule data
        data = {
            "sensor_id": sensor.id,
            "name": "Stop sensor",
            "start_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "end_time": (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%dT%H:%M:%S'),
            "action": "stop",
        }

        response = self.client.post(
            "/schedules",
            headers=headers,
            json=data,
        )
        self.assertEqual(response.status_code, 201)
        expected_message = {"message": "Sensor Schedule created successfully"}
        self.assertEqual(response.json, expected_message)

    def test_edit_sensor_schedule(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Schedule
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_schedule = SensorScheduleFactory(sensor_id=sensor.id, user_id=user.id)

        # Edit the sensor schedule
        edit_data = {
            "sensor_id": sensor.id,
            "name": "Start sensor",
            "start_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "end_time": (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%dT%H:%M:%S'),
            "action": "start",
        }
        response_edit = self.client.put(
            f"/schedules/{sensor_schedule.id}",
            headers=headers,
            json=edit_data,
        )
        self.assertEqual(response_edit.status_code, 200)
        expected_message = {"message": "Sensor Schedule updated successfully"}
        self.assertEqual(response_edit.json, expected_message)

    def test_delete_sensor_schedule(self):
        user = UserFactory()
        user_token = generate_token(user)
        headers = {"Authorization": f"Bearer {user_token}"}

        # Create Home, Room, Sensor, and Sensor Schedule
        home = HomeFactory(user_id=user.id)
        room = RoomFactory(user_id=user.id, home_id=home.id)
        sensor = SensorFactory(user_id=user.id, room_id=room.id)
        sensor_schedule = SensorScheduleFactory(sensor_id=sensor.id, user_id=user.id)

        # Delete the sensor schedule
        response = self.client.delete(
            f"/schedules/{sensor_schedule.id}",
            headers=headers
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        get_response = self.client.get(
            f"/schedules/{sensor_schedule.id}",
            headers=headers
        )
        self.assertEqual(get_response.status_code, 404)
