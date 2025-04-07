from ..utils import get_deep_value, get_deep_json, get_cl_tags


class CLValue(object):
    def __init__(self, data) -> None:
        self.data = data

    def value(self):
        return get_deep_value(self)

    def cl_value(self):
        content = self.serialize()
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')

        tag = get_cl_tags(self)
        return (bytes_len + content + tag).hex()

    def to_json(self):
        return get_deep_json(self)


class CLAtomic:
    pass
