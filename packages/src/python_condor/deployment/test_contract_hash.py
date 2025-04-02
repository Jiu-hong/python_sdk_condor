
import json
from python_condor.cl_values.cl_number import CLU256
from python_condor.cl_values.cl_string import CLString
from python_condor.deployment.deploy import Deploy
from python_condor.deployment.deploy_header import DeployHeader
from python_condor.deployment.session_contract_hash import SessionContractHash
from python_condor.deployment.session_contract_name import SessionContractName
from python_condor.deployment.session_package_name import SessionPackageName
from python_condor.deployment.session_payment import SessionPayment
from python_condor.keys.ecc_types import KeyAlgorithm


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

contract_hash = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
# runtime_args = {}
session_packagehash = SessionContractHash(
    contract_hash, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()

payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [
                ("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])

a = deploy.to_json()
print("a:", json.dumps(a))
