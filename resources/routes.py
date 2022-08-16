from resources.admin import CreateAdmin
from resources.auth import Register, Login
from resources.events import CreateEvents, EventAction, EventHint
from resources.riddles import ListCreateRiddle, RiddleDetails, PublicRiddles

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateRiddle, "/riddles"),
    (RiddleDetails, "/riddles/<int:id_>"),
    (CreateEvents, "/riddles/<int:id_>/events"),
    (EventAction, "/event"),
    (EventHint, "/event/hint/<int:current_question_>"),
    (CreateAdmin, "/admin"),
    (PublicRiddles, "/riddles/public"),
)
