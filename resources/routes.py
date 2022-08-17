from resources.admin import CreateAdmin
from resources.auth import Register, Login
from resources.discount import DiscountValidation
from resources.events import CreateEvents, EventAction, EventHint
from resources.riddles import ListCreateRiddle, RiddleDetails, PublicRiddles
from resources.transactions import CreateTransaction

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
    (DiscountValidation, "/discount/validate"),
    (CreateTransaction, "/transaction"),
)
