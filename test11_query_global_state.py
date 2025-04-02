from python_condor import QUERY_GLOBAL_STATE

url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QUERY_GLOBAL_STATE(
    url, "hash-596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b")
print(query_global_state.run())

# deploy = GetTransction(
#     url, "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8", False)
# print(deploy.run())
