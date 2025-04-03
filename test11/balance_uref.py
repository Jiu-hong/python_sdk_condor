from python_condor import QueryBalancePurseUref

state_root_hash = "e6f5ba476f83c2b8b0f5740d14e0d5535692c6e977115b998b9e144d53ae5c90"
purse = "uref-5c140dd0a3d1445387013f59318109146ed6d25bb2208b11de508b002253a4c0-007"
incorrectpurse = "xxx"

incorrct_public_key = "7e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryBalancePurseUref(
    url, purse, state_root_hash)
print(query_global_state.run())
