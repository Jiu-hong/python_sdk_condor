import pytest
from datetime import datetime
from python_condor import KeyAlgorithm, TransactionV1, TransactionV1Payload, TransactionEntryPoint, EntityAliasTarget, PricingMode, TransactionScheduling, CLOption, CLTuple3, CLString, CLBool, CLURef, RESULTHOLDER


# ===== transaction v1 =====
args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(None, CLString(RESULTHOLDER()))}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 200000000000)
target1 = EntityAliasTarget("VmCasperV1", "accesscontract")
entrypoint1 = TransactionEntryPoint("Custom", "test2")

transaction_v1payload = TransactionV1Payload(args, target1,
                                             entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test", 30, datetime.fromisoformat('2025-03-26T03:11:48.829Z'))

transactionv1 = TransactionV1(
    transaction_v1payload, [("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])

transactionv1_json = {'transaction': {'Version1': {'approvals': [{'signature': '0141b5e6ee2b5784381844a55ffc274e68ffcc28fc4a99f409e66cfae034e16c04f77622f61d885316f90c64c4dd693c99e8716ebabc341143d23cd62f45dafb09',
                                                                  'signer': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5'}],
                                                   'hash': 'f2a4859da51264535b47ab93e775672e0e38e4fe7c36596309a4e52de8f787cb',
                                                   'payload': {'chain_name': 'integration-test',
                                                               'fields': {'args': {'Named': [('arg1',
                                                                                              {'bytes': '0500000068656c6c6f01fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07',
                                                                                               'cl_type': {'Tuple3': ['String',
                                                                                                                      'Bool',
                                                                                                                      'URef']},
                                                                                                  'parsed': ('hello',
                                                                                                             True,
                                                                                                             'uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007')}),
                                                                                             ('arg2',
                                                                                              {'bytes': '00',
                                                                                               'cl_type': {'Option': 'String'},
                                                                                                  'parsed': None})]},
                                                                          'entry_point': {'Custom': 'test2'},
                                                                          'scheduling': 'Standard',
                                                                          'target': {'Stored': {'id': {'ByName': 'accesscontract'},
                                                                                                'runtime': 'VmCasperV1'}}},
                                                               'initiator_addr': {'PublicKey': '017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5'},
                                                               'pricing_mode': {'PaymentLimited': {'gas_price_tolerance': 1,
                                                                                                   'payment_amount': 200000000000,
                                                                                                   'standard_payment': True}},
                                                               'timestamp': '2025-03-26T03:11:48.829Z',
                                                               'ttl': '30m'}}}}


def test_transactionv1_to_bytes():
    result = transactionv1.byteHash()
    assert result == "f2a4859da51264535b47ab93e775672e0e38e4fe7c36596309a4e52de8f787cb"


def test_transactionv1_to_json():
    result = transactionv1.to_json()
    assert result == transactionv1_json
