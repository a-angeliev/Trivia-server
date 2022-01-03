import enum


class RoleType(enum.Enum):
    user = "user"
    admin = "admin"


class State(enum.Enum):
    available = "available"
    archived = "archived"
