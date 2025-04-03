import requests
from ....constants import RpcMethod


RPCMETHOD = RpcMethod()


class QueryBalanceMainPursePublicKeyByBlockId:
    def __init__(self, url, main_purse_under_public_key: str, block_id: int | str):
        self.url = url
        if isinstance(block_id, int):
            params = [
                {
                    "BlockHeight": block_id
                },
                {
                    "main_purse_under_public_key": main_purse_under_public_key
                }
            ]
        elif isinstance(block_id, str):
            params = [
                {
                    "BlockHash": block_id
                },
                {
                    "main_purse_under_public_key": main_purse_under_public_key
                }
            ]
        else:
            raise ValueError(
                "the block_id should be str for `BlockHash` or int for `BlockHeight`")
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.QUERY_BALANCE,
            "params": params}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()
