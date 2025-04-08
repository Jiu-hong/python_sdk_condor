from ...constants import Prefix

PREFIX = Prefix()


def check_byte_code_key_format(data):
    rest_hex = data.removeprefix(PREFIX.BYTE_CODE)
    if rest_hex.startswith(PREFIX.V1_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
    elif rest_hex.startswith(PREFIX.V2_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
    elif rest_hex.startswith(PREFIX.EMPTY):
        bytescode_hex = ""
    else:
        raise ValueError("invalid byte-code-xxx")
    try:
        bytes.fromhex(bytescode_hex)
    except:
        raise ValueError("bytescode should be hex string")


def serialize_bytes_code_key(data):
    rest_hex = data.removeprefix(PREFIX.BYTE_CODE)
    if rest_hex.startswith(PREFIX.V1_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
        value = int(1).to_bytes() + bytes.fromhex(bytescode_hex)
    elif rest_hex.startswith(PREFIX.V2_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
        value = int(2).to_bytes() + bytes.fromhex(bytescode_hex)
    else:
        value = int(0).to_bytes()
    return value
