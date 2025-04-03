from python_condor import QueryBalanceMainPurseAccountHashByBlockId

incorrect_account_hash = "xx"
account_hash = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryBalanceMainPurseAccountHashByBlockId(
    url, account_hash)
print(query_global_state.run())
