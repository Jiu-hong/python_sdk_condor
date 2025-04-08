from ...constants import Prefix

PREFIX = Prefix()


def check_era_key_format(data):
    try:
        int(data.removeprefix(PREFIX.ERA))
    except:
        raise ValueError("era value should be decimal int")


def serialize_era_key(data):
    era_int = int(data.removeprefix(PREFIX.ERA))
    value = era_int.to_bytes(8, byteorder='little')
    return value
