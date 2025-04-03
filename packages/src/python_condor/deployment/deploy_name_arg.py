from ..constants.cons_jsonname import JsonName
from ..utils import serialize_string


JSONNAME = JsonName()


class DeployNamedArg:
    def __init__(self, args):
        for arg_value in args.values():
            if not hasattr(arg_value, "tag"):
                raise ValueError("The value for NamedArg should be CLValue.")
        self.args = args

    def serialize(self) -> bytes:
        inner_serialize = b''
        for name, value in self.args.items():

            s_name = serialize_string(name)
            inner_serialize += s_name
            s_value = bytes.fromhex(value.cl_value())
            inner_serialize += s_value

        list_length = int(len(self.args)).to_bytes(4, "little")
        return list_length + inner_serialize

    def to_json(self):
        args_list = []
        for key, value in self.args.items():
            my_dict = {}
            my_dict[JSONNAME.CL_TYPE] = value.to_json()
            my_dict[JSONNAME.BYTES] = value.serialize().hex()
            my_dict[JSONNAME.PARSED] = value.value()
            args_list.append((key, my_dict))
        return args_list
