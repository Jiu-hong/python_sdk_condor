from .base import constant


class TargetKind(object):
    @constant
    def NATIVE():
        return "native"

    @constant
    def STORED():
        return "stored"

    @constant
    def SESSION():
        return "session"
