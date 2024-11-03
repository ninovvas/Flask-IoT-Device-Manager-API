from resources.auth import RegisterUser, LoginUser, LogoutUser
from resources.home import HomeListCreate, HomeDetail
from resources.room import RoomListCreate, RoomDetail

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
    (HomeListCreate, "/homes"),
    (HomeDetail, "/homes/<int:home_id>"),
    (RoomListCreate, '/rooms'),
    (RoomDetail, '/rooms/<int:room_id>')
)