from python_condor import QueryGlobalState

url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryGlobalState(
    url, "hash-596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b")
print(query_global_state.run())
