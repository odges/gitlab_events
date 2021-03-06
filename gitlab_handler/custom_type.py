from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class EventType(AutoName):
    note = auto()
    issue = auto()
    merge_request = auto()
    pipeline = auto()
    build = auto()
    deployment = auto()


class ActionType(AutoName):
    open = auto()
    close = auto()
    reopen = auto()
    update = auto()
    approved = auto()
    unapproved = auto()
    approval = auto()
    unapproval = auto()
    merge = auto()
