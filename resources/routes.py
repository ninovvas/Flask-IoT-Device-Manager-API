from resources.auth import RegisterUser, LoginUser, LogoutUser
from resources.home import HomeListCreate, HomeDetail

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
    (HomeListCreate, "/homes"),
    (HomeDetail, "/homes/<int:home_id>")
)