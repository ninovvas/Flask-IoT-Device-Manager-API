from resources.auth import RegisterUser, LoginUser, LogoutUser
from resources.home import HomeListCreate

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
    (HomeListCreate, "/homes")
)