"""
Tests for Deploy functionality.

This module contains test cases for the Deploy class, which represents
deployments in Casper transactions. The tests verify:
- Deploy creation with header, payment, and session
- Body hash generation
- Approval handling
- JSON serialization
"""

from datetime import datetime

from python_condor import (
    Deploy,
    DeployHeader,
    CLU256,
    CLString,
    KeyAlgorithm,
    SessionPackageHash,
    SessionPayment
)


# Test data setup
ACCOUNT = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
CHAIN_NAME = "integration-test"
TIMESTAMP = datetime.fromisoformat('2025-03-26T03:11:48.829Z')
TTL = 30
GAS_PRICE = 1

PACKAGE_HASH = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
ENTRYPOINT = "apple"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}

PAYMENT_AMOUNT = 2500000000
SECRET_KEY_PATH = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"


def create_test_deploy_header() -> DeployHeader:
    """
    Create a test deploy header with sample data.

    Returns:
        DeployHeader: A configured test header
    """
    return DeployHeader(
        ACCOUNT,
        CHAIN_NAME,
        TIMESTAMP,
        ttl=TTL,
        gas_price=GAS_PRICE
    )


def create_test_session_package_hash() -> SessionPackageHash:
    """
    Create a test session package hash with sample data.

    Returns:
        SessionPackageHash: A configured test session
    """
    return SessionPackageHash(
        PACKAGE_HASH,
        None,
        ENTRYPOINT,
        RUNTIME_ARGS
    )


def create_test_deploy() -> Deploy:
    """
    Create a test deploy with sample data.

    Returns:
        Deploy: A configured test deploy
    """
    header = create_test_deploy_header()
    payment = SessionPayment(PAYMENT_AMOUNT)
    session = create_test_session_package_hash()

    return Deploy(
        header,
        payment,
        session,
        [(SECRET_KEY_PATH, KeyAlgorithm.ED25519)]
    )


# Expected test results
EXPECTED_APPROVALS = {
    'approvals': [{
        'signer': ACCOUNT,
        'signature': '016a91e75b282731b79abd416bf902cffd3a950a880045a35c73cbad2393a6803cf2ef4a25ce9be53fed4c3571b1964fd033411195dc2f3a7ecb93f550ccef5701'
    }]
}

EXPECTED_JSON = {
    'deploy': {
        'hash': '25a945fc2882ae92e4ffe7b5301d57a6d0ee1ee203fd1aa133992f2e03341ad6',
        'header': {
            'account': ACCOUNT,
            'timestamp': '2025-03-26T03:11:48.829Z',
            'ttl': f'{TTL}m',
            'gas_price': GAS_PRICE,
            'body_hash': 'cff3320bf0cfc054db512a86040528b730a229ec22c83b201e4daf0f6ead5832',
            'dependencies': [],
            'chain_name': CHAIN_NAME
        },
        'payment': {
            'ModuleBytes': {
                'module_bytes': '',
                'args': [
                    ('amount', {
                        'cl_type': 'U512',
                        'bytes': '0400f90295',
                        'parsed': PAYMENT_AMOUNT
                    })
                ]
            }
        },
        'session': {
            'StoredVersionedContractByHash': {
                'hash': PACKAGE_HASH,
                'version': None,
                'entry_point': ENTRYPOINT,
                'args': [
                    ('arg1', {
                        'cl_type': 'U256',
                        'bytes': '017b',
                        'parsed': 123
                    }),
                    ('arg2', {
                        'cl_type': 'String',
                        'bytes': '0500000068656c6c6f',
                        'parsed': 'hello'
                    })
                ]
            }
        },
        'approvals': [{
            'signer': ACCOUNT,
            'signature': '0117465156d2b48f96a9322d2c6c47945b5c568c2db34f24ec7449ca834b28ffd5f82b6dcfe183fee523c7c6a2577f71112921d18ff0d6ace3bc65ea6c011aeb0b'
        }]
    }
}


def test_deploy_generate_body_hash():
    """
    Test body hash generation for a deploy.

    Verifies that the deploy correctly generates and stores a body hash.
    """
    deploy = create_test_deploy()
    assert not hasattr(deploy.header, "body_hash")
    deploy.generate_body_hash()
    assert hasattr(deploy.header, "body_hash")


def test_deploy_get_approvals():
    """
    Test approval generation for a deploy.

    Verifies that the deploy correctly generates approvals with the expected format.
    """
    deploy = create_test_deploy()
    result = deploy.get_approvals(
        "e9e91ddf3b077615a9ebd3ce69b5f1b79ebae8c1ffac81615a0d351b02378340"
    )
    assert result == EXPECTED_APPROVALS


def test_deploy_to_json():
    """
    Test JSON serialization of a deploy.

    Verifies that the deploy correctly serializes to the expected JSON structure.
    """
    deploy = create_test_deploy()
    result = deploy.to_json()
    assert result == EXPECTED_JSON
