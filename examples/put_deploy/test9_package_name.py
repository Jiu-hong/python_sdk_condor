from python_condor import CLU256, CLString, PutDeploy, Deploy, DeployHeader, SessionPackageName, SessionPayment, KeyAlgorithm


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

package_hash_name = "my_hash"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_packagehash = SessionPackageName(
    package_hash_name, None, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()

payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [
                ("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem", KeyAlgorithm.ED25519)])

url = "http://node.integration.casper.network:7777/rpc"
deploy_result = PutDeploy(url, deploy.to_json()).run()
print(deploy_result)
