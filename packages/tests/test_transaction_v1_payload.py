import pytest
from datetime import datetime
from python_condor import TransactionV1Payload, TransactionEntryPoint, EntityAliasTarget, PricingMode, TransactionScheduling, CLOption, CLTuple3, CLString, CLBool, CLURef, RESULTHOLDER


# ===== transaction v1payload =====


args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(None, CLString(RESULTHOLDER()))}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 200000000000)
target1 = EntityAliasTarget("VmCasperV1", "accesscontract")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")

transaction_v1payload = TransactionV1Payload(args, target1,
                                             entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test", 30, datetime.fromisoformat('2025-03-26T03:11:48.829Z'))

payload_json = {'payload': {'chain_name': 'integration-test',
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
                            'ttl': '30m'}}


def test_transaction_v1payload_to_bytes():
    result = transaction_v1payload.to_bytes().hex()
    assert result == "0600000000000000000001003600000002003e00000003004600000004005a0000000500850000006e010000020000000000000000000100010000002200000000017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f55d486fd09501000040771b000000000010000000696e746567726174696f6e2d746573740400000000000000000001000100000002000900000003000a0000000b0000000000d0ed902e00000001010400000000004f000000000200000004000000617267312b0000000500000068656c6c6f01fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07140a000c040000006172673201000000000d0a0100510000000300000000000000000001000100000002002800000037000000010200000000000000000001000100000013000000010e000000616363657373636f6e747261637401000000000000000000010000000002001e000000020000000000000000000100010000000a0000000105000000746573743203000f000000010000000000000000000100000000"


def test_transaction_v1payload_to_json():
    result = transaction_v1payload.to_json()
    assert result == payload_json
