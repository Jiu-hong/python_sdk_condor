import requests

from ..constants import RpcMethod
# from ..constants import RpcMethod

RPCMETHOD = RpcMethod()

# url = 'http://node.integration.casper.network:7777/rpc'
# transaction = {'transaction': {'Version1': {'hash': '2f6e8bd96a91e5f2cd3a2720808172c6c3facd2ea531af471b0a2b93c7961ca2', 'payload': {'initiator_addr': {'PublicKey': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5'}, 'timestamp': '2025-03-30T08:53:00.103Z', 'ttl': '30m', 'chain_name': 'integration-test', 'pricing_mode': {'PaymentLimited': {'payment_amount': 200000000000, 'gas_price_tolerance': 1, 'standard_payment': True}}, 'fields': {'args': {'Named': [('arg1', {'cl_type': {'Tuple3': ['String', 'Bool', 'URef']}, 'bytes': '0500000068656c6c6f01fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07', 'parsed': (
#     'hello', True, 'uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007')})]}, 'entry_point': {'Custom': 'test2'}, 'scheduling': 'Standard', 'target': {'Stored': {'id': {'ByName': 'accesscontract'}, 'runtime': 'VmCasperV1'}}}}, 'approvals': [{'signer': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5', 'signature': '0134ff9003c5e7e25087ee7760b680e12cbbf22b5db002b85e1fe94b1d0ac600259ccf6390aa618cdc64f9ad9accf656edd578a25da3ab9c1f9832305443216206'}]}}}
# print("type:", type(transaction))

# x = requests.post(url, json=rpc_payload)
# result = x.json()
# print(result)


class PutDeploy:
    def __init__(self, url, deploy: dict):
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_DEPLOY,
            "params": deploy}

    def run(self):
        x = requests.post(self.url, json=self.rpc_payload)
        return x.json()


# transaction_v1 = {'transaction': {'Version1': {'hash': '57fbbd918450126a48ef2b0c704a05ee9f6673fab27cac4ad3cc2d2d88fd214b', 'payload': {'initiator_addr': {'PublicKey': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5'}, 'timestamp': '2025-03-30T09:11:46.601Z', 'ttl': '30m', 'chain_name': 'integration-test', 'pricing_mode': {'PaymentLimited': {'payment_amount': 200000000000, 'gas_price_tolerance': 1, 'standard_payment': True}}, 'fields': {'args': {'Named': [('arg1', {'cl_type': {'Tuple3': ['String', 'Bool', 'URef']}, 'bytes': '0500000068656c6c6f01fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07', 'parsed': (
#     'hello', True, 'uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007')})]}, 'entry_point': {'Custom': 'test2'}, 'scheduling': 'Standard', 'target': {'Stored': {'id': {'ByName': 'accesscontract'}, 'runtime': 'VmCasperV1'}}}}, 'approvals': [{'signer': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5', 'signature': '01ce6613eb5dfa1d1cb4fc6e6ea6a5a79a614d481f28bbeb43c072ad49cc343f27aab626e0a120a2ee928ad024516b6674384648ef23718c9454d2ecd910a6c10f'}]}}}
# a = PutTransction(transaction_v1)
# a.run()
