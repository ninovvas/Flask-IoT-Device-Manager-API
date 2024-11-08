from resources.auth import RegisterUser, LoginUser, LogoutUser
from resources.home import HomeListCreate, HomeDetail
from resources.room import RoomListCreate, RoomDetail
from resources.sensor import SensorListCreate, SensorDetail
from resources.sensor_data import SensorDataListCreate, SensorDataDetail
from resources.sensor_schedule import SensorScheduleListCreate, SensorScheduleDetail
from resources.sensor_statistic import SensorStatisticListCreate, SensorStatisticDetail
from resources.user import User

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
    (HomeListCreate, "/homes"),
    (HomeDetail, "/homes/<int:home_id>"),
    (RoomListCreate, "/rooms"),
    (RoomDetail, "/rooms/<int:room_id>"),
    (SensorListCreate, "/sensors"),
    (SensorDetail, "/sensors/<int:sensor_id>"),
    (SensorDataListCreate, "/sensor_data"),
    (SensorDataDetail, "/sensor_data/<int:sensor_data_id>"),
    (SensorScheduleListCreate, "/schedules"),
    (SensorScheduleDetail, "/schedules/<int:sensor_schedule_id>"),
    (SensorStatisticListCreate, "/statistics"),
    (SensorStatisticDetail, "/statistics/<int:sensor_statistic_id>"),
    (User, "/admins/users"),
)
