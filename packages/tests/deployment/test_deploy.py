from datetime import datetime

from python_condor import DeployHeader, Deploy, CLU256, CLString, KeyAlgorithm, SessionPackageHash, SessionPayment


# todo
# ===== DeployHeader =====
account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(account, chain_name,
                      datetime.fromisoformat('2025-03-26T03:11:48.829Z'), ttl=30, gas_price=1)

package_hash_hex = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}

session_packagehash = SessionPackageHash(
    package_hash_hex, None, entrypoint, runtime_args)


payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [
                ("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem", KeyAlgorithm.ED25519)])


# === generate_body_hash() ===
def test_deploy_generate_body_hash():
    assert not hasattr(deploy.header, "body_hash")
    deploy.generate_body_hash()
    assert hasattr(deploy.header, "body_hash")


# ====get_approvals() ===
def test_deploy_get_approvals():
    result = deploy.get_approvals(
        "e9e91ddf3b077615a9ebd3ce69b5f1b79ebae8c1ffac81615a0d351b02378340")
    assert result == {'approvals': [{'signer': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5',
                                     'signature': '016a91e75b282731b79abd416bf902cffd3a950a880045a35c73cbad2393a6803cf2ef4a25ce9be53fed4c3571b1964fd033411195dc2f3a7ecb93f550ccef5701'}]}


# ====to_json() ===
def test_deploy_to_json():
    result = deploy.to_json()
    print("result:", result)
    assert result == {'deploy': {'hash': '25a945fc2882ae92e4ffe7b5301d57a6d0ee1ee203fd1aa133992f2e03341ad6', 'header': {'account': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5', 'timestamp': '2025-03-26T03:11:48.829Z', 'ttl': '30m', 'gas_price': 1, 'body_hash': 'cff3320bf0cfc054db512a86040528b730a229ec22c83b201e4daf0f6ead5832', 'dependencies': [], 'chain_name': 'integration-test'}, 'payment': {'ModuleBytes': {'module_bytes': '', 'args': [('amount', {'cl_type': 'U512', 'bytes': '0400f90295', 'parsed': 2500000000})]}}, 'session': {'StoredVersionedContractByHash': {'hash': '051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6', 'version': None, 'entry_point': 'apple', 'args': [(
        'arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}, 'approvals': [{'signer': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5', 'signature': '0117465156d2b48f96a9322d2c6c47945b5c568c2db34f24ec7449ca834b28ffd5f82b6dcfe183fee523c7c6a2577f71112921d18ff0d6ace3bc65ea6c011aeb0b'}]}}
