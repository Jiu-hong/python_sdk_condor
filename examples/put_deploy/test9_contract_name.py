from python_condor import CLU256, CLString, Deploy, DeployHeader, SessionContractName, SessionPayment, KeyAlgorithm, PutDeploy


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

contract_name = "apple_contract"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_packagehash = SessionContractName(
    contract_name, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()

payment = SessionPayment(2500000000)

keys = [("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem",
         KeyAlgorithm.ED25519)]
deploy = Deploy(header, payment, session_packagehash, keys)


url = "http://node.integration.casper.network:7777/rpc"
deploy_result = PutDeploy(url, deploy.to_json()).run()
print(deploy_result)
