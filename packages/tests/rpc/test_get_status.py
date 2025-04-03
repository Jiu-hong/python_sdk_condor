from python_condor import GetStatus


url = "http://node.integration.casper.network:7777/rpc"
block_id = 4842751
block_hash = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"
query_global_state = GetStatus(url)
print(query_global_state.run())
