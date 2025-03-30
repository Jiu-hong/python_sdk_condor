from .base import constant


class SchedulingKind(object):
    @constant
    def STANDARD():
        return "Standard"


CONST = SchedulingKind()
print(CONST.STANDARD)
