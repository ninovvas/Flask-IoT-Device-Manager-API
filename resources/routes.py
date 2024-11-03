from resources.auth import RegisterUser, LoginUser, LogoutUser
from resources.home import HomeListCreate, HomeDetail
from resources.room import RoomListCreate, RoomDetail
from resources.sensor import SensorListCreate, SensorDetail
from resources.sensor_data import SensorDataListCreate, SensorDataDetail

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
    (HomeListCreate, "/homes"),
    (HomeDetail, "/homes/<int:home_id>"),
    (RoomListCreate, '/rooms'),
    (RoomDetail, '/rooms/<int:room_id>'),
    (SensorListCreate, '/sensors'),
    (SensorDetail, '/sensors/<int:sensor_id>'),
    (SensorDataListCreate, '/sensor_data'),
    (SensorDataDetail, '/sensor_data/<int:sensor_data_id>')
)