
from python_condor import GetReward


url = "http://node.integration.casper.network:7777/rpc"
validator = "0115c9b40c06ff99b0cbadf1140b061b5dbf92103e66a6330fbcc7768f5219c1ce"
delegagor = "01005e50796e225c0f6aa0d61c0fa0bda5af8aa23c194414bf2bbed1e0a774f2a6"
query_global_state = GetReward(url, validator, delegagor, 17430)
print(query_global_state.run())
