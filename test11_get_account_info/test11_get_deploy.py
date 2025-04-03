from python_condor import GetDeploy


pk = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
url = "http://node.integration.casper.network:7777/rpc"
block_id = 4842751
deploy_hash = "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8"
query_global_state = GetDeploy(url, deploy_hash)
print(query_global_state.run())
