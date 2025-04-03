from python_condor import EntityAliasTarget


# ===== EntityAliasTarget =====
target = EntityAliasTarget("VmCasperV1", "apple_contract")


def test_targetnoversion_to_bytes():
    result = target.to_bytes().hex()
    assert result == "0300000000000000000001000100000002002800000037000000010200000000000000000001000100000013000000010e0000006170706c655f636f6e7472616374010000000000000000000100000000"


def test_targetnoversion_to_json():
    result = target.to_json()
    assert result == {'target': {'Stored': {'id': {'ByName': 'apple_contract'},
                                            'runtime': 'VmCasperV1'}}}
