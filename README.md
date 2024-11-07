
# Flask IoT Device Manager

A RESTful API for managing IoT devices, sensors, homes, rooms, and their associated data. This API allows you to register and authenticate users, manage sensor data, and track statistics over time.

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd flask_iot_device_manager
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Application**
   Modify the `config.py` file if necessary to adjust for your database or environment settings.

4. **Initialize the Database**
   ```bash
   python db.py
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

   The application should now be running at `http://127.0.0.1:5000`.

## Project Structure

- **app.py**: Entry point for the Flask application.
- **config.py**: Configuration settings (e.g., database URI).
- **db.py**: Handles database initialization and migrations.
- **requirements.txt**: List of dependencies.
- **managers**: Contains various managers for handling business logic related to authentication, devices, homes, rooms, sensors, sensor data, schedules, statistics, and users.

## API Endpoints

### Authentication

#### Register a New User
- **Endpoint**: `POST /register`
- **Example Request**:
  ```json
  {
      "username": "new_user",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "message": "User registered successfully"
  }
  ```

#### Login
- **Endpoint**: `POST /login`
- **Example Request**:
  ```json
  {
      "username": "new_user",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "access_token": "<JWT_TOKEN>"
  }
  ```

#### Logout
- **Endpoint**: `POST /logout`
- **Example Request**:
  ```json
  {}
  ```
- **Response**:
  ```json
  {
      "message": "Successfully logged out"
  }
  ```

### Homes

#### Create a New Home
- **Endpoint**: `POST /homes`
- **Example Request**:
  ```json
  {
      "address": "123 IoT Street",
      "city": "Techville",
      "state": "CA",
      "zip_code": "94000"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "address": "123 IoT Street",
      "city": "Techville",
      "state": "CA",
      "zip_code": "94000"
  }
  ```

#### Get All Homes
- **Endpoint**: `GET /homes`
- **Response**:
  ```json
  [
      {
          "id": 1,
          "address": "123 IoT Street",
          "city": "Techville",
          "state": "CA",
          "zip_code": "94000"
      }
  ]
  ```

#### Get a Specific Home
- **Endpoint**: `GET /homes/<home_id>`
- **Example**: `GET /homes/1`
- **Response**:
  ```json
  {
      "id": 1,
      "address": "123 IoT Street",
      "city": "Techville",
      "state": "CA",
      "zip_code": "94000"
  }
  ```

#### Update a Home
- **Endpoint**: `PUT /homes/<home_id>`
- **Example**: `PUT /homes/2`
- **Request**:
  ```json
  {
      "address": "456 Smart Lane",
      "city": "Techville",
      "state": "CA",
      "zip_code": "94001"
  }
  ```
- **Response**:
  ```json
  {
      "id": 2,
      "address": "456 Smart Lane",
      "city": "Techville",
      "state": "CA",
      "zip_code": "94001"
  }
  ```

#### Delete a Home
- **Endpoint**: `DELETE /homes/<home_id>`
- **Example**: `DELETE /homes/10`
- **Response**:
  ```json
  {
      "message": "Home deleted successfully"
  }
  ```

### Rooms

#### Create a New Room
- **Endpoint**: `POST /rooms`
- **Example Request**:
  ```json
  {
      "name": "Living Room",
      "description": "Main living area",
      "home_id": 1
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Living Room",
      "description": "Main living area",
      "home_id": 1
  }
  ```

#### Get All Rooms
- **Endpoint**: `GET /rooms`
- **Response**:
  ```json
  [
      {
          "id": 1,
          "name": "Living Room",
          "description": "Main living area",
          "home_id": 1
      }
  ]
  ```

#### Get a Specific Room
- **Endpoint**: `GET /rooms/<room_id>`
- **Example**: `GET /rooms/1`
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Living Room",
      "description": "Main living area",
      "home_id": 1
  }
  ```

#### Update a Room
- **Endpoint**: `PUT /rooms/<room_id>`
- **Example**: `PUT /rooms/room_id`
- **Request**:
  ```json
  {
      "name": "Updated Room",
      "description": "Updated description"
  }
  ```
- **Response**:
  ```json
  {
      "id": "room_id",
      "name": "Updated Room",
      "description": "Updated description",
      "home_id": 1
  }
  ```

#### Delete a Room
- **Endpoint**: `DELETE /rooms/<room_id>`
- **Example**: `DELETE /rooms/room_id`
- **Response**:
  ```json
  {
      "message": "Room deleted successfully"
  }
  ```
