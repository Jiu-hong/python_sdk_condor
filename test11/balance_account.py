from python_condor import QueryBalanceMainPurseAccountHash

incorrect_account_hash = "account-hash-xxx"
state_root_hash = "2c8c6983cc59e26f0722ec53b5153f5ba42c6de3e76c1b0f6d5fbc1f9625d43c"
account_hash = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
url = "http://node.integration.casper.network:7777/rpc"
query_global_state = QueryBalanceMainPurseAccountHash(
    url, account_hash)
print(query_global_state.run())
