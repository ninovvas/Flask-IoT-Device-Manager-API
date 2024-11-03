
# Flask IoT Device Manager

A Flask-based application for managing IoT devices within rooms, supporting CRUD operations for users, rooms, sensors, and authentication.

## Project Structure
- **app.py**: Initializes the Flask app and database connection.
- **config.py**: Manages configuration settings.
- **db.py**: Database initialization and session handling.
- **managers/**: Contains the main logic for handling CRUD operations on devices, rooms, and sensors.
- **models/**: Defines the ORM models for database tables.
- **requirements.txt**: Lists dependencies for the project.

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL or any compatible SQL database

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask_iot_device_manager.git
   cd flask_iot_device_manager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root with the following:
   ```plaintext
   CONFIG_ENV=development
   DATABASE_URL=your_database_url
   SECRET_KEY=your_secret_key
   ```

4. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Authentication
1. **Login**  
   - **Endpoint**: `POST /auth/login`
   - **Body**: `{ "username": "user", "password": "pass" }`
   - **Response**: `{ "token": "JWT_TOKEN" }`

2. **Logout**  
   - **Endpoint**: `POST /auth/logout`
   - **Response**: `Successfully logged out`

### Rooms

1. **Get All Rooms**
   - **Endpoint**: `GET /rooms`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: List of all rooms associated with the user.

2. **Create Room**
   - **Endpoint**: `POST /rooms`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Body**:
     ```json
     {
       "name": "Living Room",
       "description": "Main room",
       "home_id": 1
     }
     ```
   - **Response**: Created room object.

3. **Get Room by ID**
   - **Endpoint**: `GET /rooms/{room_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: Details of the specified room.

4. **Update Room**
   - **Endpoint**: `PUT /rooms/{room_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Body**:
     ```json
     {
       "name": "Updated Living Room",
       "description": "Updated description",
       "home_id": 1
     }
     ```
   - **Response**: Updated room object.

5. **Delete Room**
   - **Endpoint**: `DELETE /rooms/{room_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: Confirmation message for successful deletion.

### Sensors

1. **Get All Sensors**
   - **Endpoint**: `GET /sensors`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: List of all sensors associated with the user.

2. **Create Sensor**
   - **Endpoint**: `POST /sensors`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Body**:
     ```json
     {
       "name": "Temperature Sensor",
       "room_id": 1,
       "type": "Temperature"
     }
     ```
   - **Response**: Created sensor object.

3. **Get Sensor by ID**
   - **Endpoint**: `GET /sensors/{sensor_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: Details of the specified sensor.

4. **Update Sensor**
   - **Endpoint**: `PUT /sensors/{sensor_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Body**:
     ```json
     {
       "name": "Updated Temperature Sensor",
       "room_id": 2,
       "type": "Temperature"
     }
     ```
   - **Response**: Updated sensor object.

5. **Delete Sensor**
   - **Endpoint**: `DELETE /sensors/{sensor_id}`
   - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
   - **Response**: Confirmation message for successful deletion.

## Additional Notes

- All endpoints require a valid JWT token obtained via the login endpoint.
- Use the `SECRET_KEY` in your `.env` file to securely sign and verify JWT tokens.
- The `RoomManager` and `SensorManager` classes provide methods for creating, retrieving, updating, and deleting entries in the database.
