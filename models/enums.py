import enum


class RoleType(enum.Enum):
    user = "user"
    admin = "admin"
    public = "public"


class State(enum.Enum):
    available = "available"
    archived = "archived"
