from python_condor import QueryGlobalStateByBlockId

key1 = "hash-596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
key2 = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
key3 = "uref-15451be7efc662bd21a5ea01b0d4d6c6b81618436f02400fd63bde30eee2454c-007"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryGlobalStateByBlockId(
    url, key3)
print(query_global_state.run())
