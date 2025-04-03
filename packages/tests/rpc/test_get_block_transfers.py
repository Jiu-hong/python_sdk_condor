from python_condor import GetBlockTransfers


pk = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
url = "http://node.integration.casper.network:7777/rpc"
block_id = 4842751
block_hash = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"
query_global_state = GetBlockTransfers(url)
print(query_global_state.run())
