from python_condor import GetAccountInfoByPublicKey

incorrect_pk = "12345"
pk = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = GetAccountInfoByPublicKey(
    url, pk, "12345")
print(query_global_state.run())
