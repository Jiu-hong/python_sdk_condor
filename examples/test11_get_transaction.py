from python_condor import GetTransction

url = "http://node.integration.casper.network:7777/rpc"
transaction = GetTransction(
    url, "7634c66a7c17ea96f10828cca6bf7010b29a8147fea93dce004a12e433729994")
print(transaction.run())

deploy = GetTransction(
    url, "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8", False)
print(deploy.run())
