from python_condor import GetPackage


contract_package = "contract-package-051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
incorrect_contract_package = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"

url = "http://node.integration.casper.network:7777/rpc"
block_id = 4842751
block_hash = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"

query_global_state = GetPackage(url, contract_package)
print(query_global_state.run())
