from resources.auth import Register, Login
from resources.riddles import ListCreateRiddle, RiddleDetails

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateRiddle, "/admins/riddles"),
    (RiddleDetails, "/admins/riddles/<int:id_>"),
)
