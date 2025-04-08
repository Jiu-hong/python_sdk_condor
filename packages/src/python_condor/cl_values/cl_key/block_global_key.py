BLOCK_KEY = ("block-time-00000000000000000000000000000000000000000000000000000000000000",
             "block-message-count-00000000000000000000000000000000000000000000000000000000000000")


BLOCK_MESSAGE_COUNT = "block-message-count-"


def check_block_global_key_format(data):
    if data not in BLOCK_KEY:
        raise ValueError(
            "Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'")


def serialize_block_global_key(data):
    if data.startswith(BLOCK_MESSAGE_COUNT):
        return bytes.fromhex("01") + bytes.fromhex(data.removeprefix("block-message-count-"))
    else:
        return bytes.fromhex("00") + bytes.fromhex(data.removeprefix("block-time-"))
