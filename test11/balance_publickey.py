from python_condor import QueryBalanceMainPursePublicKey

state_root_hash = "e6f5ba476f83c2b8b0f5740d14e0d5535692c6e977115b998b9e144d53ae5c90"
public_key = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
incorrct_public_key = "7e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryBalanceMainPursePublicKey(
    url, public_key)
print(query_global_state.run())
