def serialize_string(data) -> bytes:
    content = bytearray(data, encoding="utf-8")
    bytes_len = int(len(content)).to_bytes(4, byteorder='little')
    return bytes_len+content
