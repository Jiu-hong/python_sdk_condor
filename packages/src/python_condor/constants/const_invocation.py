from .base import constant


class InvocationKind(object):
    @constant
    def INVOCABLEENTITY():
        return "InvocableEntity"

    @constant
    def INVOCABLEENTITYALIAS():
        return "InvocableEntityAlias"

    @constant
    def PACKAGE():
        return "Package"

    @constant
    def PACKAGEALIAS():
        return "PackageAlias"
