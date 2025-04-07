import requests
from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class PutTransction:
    def __init__(self, url, transactionV1: dict):
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_TRANSACTION,
            "params": transactionV1}

    def run(self):
        error = {}
        try:
            x = requests.post(self.url, json=self.rpc_payload)
        except requests.exceptions.Timeout:
            error = {"err": "..Timeout.."}
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            error = {"err": "..TooManyRedirects.."}
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            error = {"err": "..RequestException.."}
        except requests.exceptions as e:
            error = {"err": e}

        else:
            if x.status_code == requests.codes.ok:
                return x.json()
            else:
                return error
