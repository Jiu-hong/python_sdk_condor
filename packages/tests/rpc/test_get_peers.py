from python_condor import GetPeers


url = "http://node.integration.casper.network:7777/rpc"

query_global_state = GetPeers(url)
print(query_global_state.run())
