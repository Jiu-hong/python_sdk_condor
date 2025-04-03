from python_condor import GetDeploy


url = "http://node.integration.casper.network:7777/rpc"

deploy = GetDeploy(
    url, "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8")
print(deploy.run())
