
import json
from python_condor.cl_values.cl_number import CLU256
from python_condor.cl_values.cl_string import CLString
from python_condor.deployment.deploy import Deploy
from python_condor.deployment.deploy_header import DeployHeader
from python_condor.deployment.session_contract_name import SessionContractName
from python_condor.deployment.session_package_name import SessionPackageName
from python_condor.deployment.session_payment import SessionPayment
from python_condor.keys.ecc_types import KeyAlgorithm
from python_condor.rpc.put_deploy import PutDeploy


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
timestamp = "123"
ttl = 30
gas_price = 1
# body_hash = "889135da6f70c3e5832a43b358a4b634df9056d4f55c9486cc92249d2c3e386d"
dependencies = "00"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

contract_name = "apple_contract"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
# runtime_args = {}
session_packagehash = SessionContractName(
    contract_name, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()

payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [
                ("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])

# a = deploy.to_json()
# print("a:", json.dumps(a))
url = "http://node.integration.casper.network:7777/rpc"
deploy_result = PutDeploy(url, deploy.to_json()).run()
print(deploy_result)
