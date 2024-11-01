from resources.auth import RegisterUser, LoginUser, LogoutUser

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (LogoutUser, "/logout"),
)