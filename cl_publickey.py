import re

from cl_baseType import CLAtomic, CLType
from cl_util import deep_value_v2


class CLPublicKey(CLType, CLAtomic):
    tag = 22

    def serialize(self):
        regx = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(self.data)
        # print(result)
        if not isinstance(result, re.Match):
            # incorrect publickey should be 01xxx(64length) or 02xxx(66length)
            raise
        return bytes.fromhex(self.data)

    def cl_value(self):

        content = self.serialize().hex()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


a = CLPublicKey(
    "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1")
print(a.serialize())
print(a)
print(a.cl_value())
# (01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})
# re.compile("(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})")
# p = re.compile("(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})")
# p.fullmatch("010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf52f5045ad6c9838d2f")
# # <re.Match object; span = (0, 66), match ='010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf5>
# q = p.fullmatch(
#     "010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf52f5045ad6c9838d2f00")
# if not isinstance(q, re.Match):
#     raise  # incorrect publickey should be 01xxx(64length) or 02xxx(66length)

# {
#     "cl_type": "PublicKey",
#     "bytes": "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1",
#     "parsed": "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1"
# }
