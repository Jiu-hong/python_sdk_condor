
from python_condor import CLU256, CLString, Deploy, DeployHeader, SessionModuleBytes, SessionPayment, KeyAlgorithm, PutDeploy


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

f = open("/Users/jh/mywork/python_sdk_condor/wasm")
module_bytes = f.read()

runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_module_bytes = SessionModuleBytes(
    module_bytes, runtime_args)


payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_module_bytes, [
                ("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])


url = "http://node.integration.casper.network:7777/rpc"
deploy_result = PutDeploy(url, deploy.to_json()).run()
print(deploy_result)
