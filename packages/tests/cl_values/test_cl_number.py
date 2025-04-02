import pytest

from python_condor import CLI32, CLI64, CLU128, CLU16, CLU256, CLU32, CLU512, CLU64, CLU8, CLBool, RESULTHOLDER

# ===== CLBool =====
# True
clbool_true = CLBool(True)


def test_true_serialize():
    result = clbool_true.serialize().hex()
    assert result == "01"


def test_true_value():
    result = clbool_true.value()
    assert result == True


def test_true_cl_value():
    result = clbool_true.cl_value()
    assert result == "010000000100"


def test_true_to_json():
    result = clbool_true.to_json()
    assert result == "Bool"


# other type than bool
def test_inner_not_bool():
    with pytest.raises(TypeError, match="Invalid type of input: <class 'str'> for CLBool. Allowed value is <class 'bool'>"):
        _ = CLBool("somethingeelse")
    with pytest.raises(TypeError, match="Invalid type of input: <class 'int'> for CLBool. Allowed value is <class 'bool'>"):
        _ = CLBool(1)


# ====== False
clbool_false = CLBool(False)


def test_false_serialize():
    result = clbool_false.serialize().hex()
    assert result == "00"


def test_false_value():
    result = clbool_false.value()
    assert result == False


def test_false_cl_value():
    result = clbool_false.cl_value()
    assert result == "010000000000"


def test_false_to_json():
    result = clbool_false.to_json()
    assert result == "Bool"

# ==== RESULTHOLDER


result_holder_clbool = CLBool(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clbool.to_json()
    assert result == "Bool"


# ===== CLI32 =====
#
cli32_value = CLI32(123)


def test_cli32_serialize():
    result = cli32_value.serialize().hex()
    assert result == "7b000000"


def test_cli32_value():
    result = cli32_value.value()
    assert result == 123


def test_cli32_cl_value():
    result = cli32_value.cl_value()
    assert result == "040000007b00000001"


def test_cli32_to_json():
    result = cli32_value.to_json()
    assert result == "I32"


# the range goes out of -2**31 - 2**31-1
def test_cli32_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be -2147483648 - 2147483647"):
        _ = CLI32(2**31-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be -2147483648 - 2147483647"):
        _ = CLI32(-2**31 - 1)


# ==== RESULTHOLDER
result_holder_cli32 = CLI32(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_cli32.to_json()
    assert result == "I32"


# ===== CLI64 =====
cli64_value = CLI64(123)


def test_cli64_serialize():
    result = cli64_value.serialize().hex()
    assert result == "7b00000000000000"


def test_cli64_value():
    result = cli64_value.value()
    assert result == 123


def test_cli64_cl_value():
    result = cli64_value.cl_value()
    assert result == "080000007b0000000000000002"


def test_cli64_to_json():
    result = cli64_value.to_json()
    assert result == "I64"


# the range goes out of -2**31 - 2**31-1
def test_cli64_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be -9223372036854775808 - 9223372036854775807"):
        _ = CLI64(2**63-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be -9223372036854775808 - 9223372036854775807"):
        _ = CLI64(-2**63 - 1)


# ==== RESULTHOLDER
result_holder_cli64 = CLI64(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_cli64.to_json()
    assert result == "I64"


# ===== CLU8 =====
clu8_value = CLU8(123)


def test_clu8_serialize():
    result = clu8_value.serialize().hex()
    assert result == "7b"


def test_clu8_value():
    result = clu8_value.value()
    assert result == 123


def test_clu8_cl_value():
    result = clu8_value.cl_value()
    assert result == "010000007b03"


def test_clu8_to_json():
    result = clu8_value.to_json()
    assert result == "U8"


# the range goes out of 0 - 255
def test_clu8_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 255"):
        _ = CLU8(2**8-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 255"):
        _ = CLU8(-1)


# ==== RESULTHOLDER
result_holder_clu8 = CLU8(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu8.to_json()
    assert result == "U8"


# ===== CLU16 =====
clu16_value = CLU16(123)


def test_clu16_serialize():
    result = clu16_value.serialize().hex()
    assert result == "7b00"


# ===== CLU32 =====
clu32_value = CLU32(123)


def test_clu32_serialize():
    result = clu32_value.serialize().hex()
    assert result == "7b000000"


def test_clu32_value():
    result = clu32_value.value()
    assert result == 123


def test_clu32_cl_value():
    result = clu32_value.cl_value()
    assert result == "040000007b00000004"


def test_clu32_to_json():
    result = clu32_value.to_json()
    assert result == "U32"


# the range goes out of 0 - 4294967295
def test_clu32_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 4294967295"):
        _ = CLU32(2**32-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 4294967295"):
        _ = CLU32(-1)


# ==== RESULTHOLDER
result_holder_clu32 = CLU32(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu32.to_json()
    assert result == "U32"


# ===== CLU64 =====
clu64_value = CLU64(123)


def test_clu64_serialize():
    result = clu64_value.serialize().hex()
    assert result == "7b00000000000000"


def test_clu64_value():
    result = clu64_value.value()
    assert result == 123


def test_clu64_cl_value():
    result = clu64_value.cl_value()
    assert result == "080000007b0000000000000005"


def test_clu64_to_json():
    result = clu64_value.to_json()
    assert result == "U64"


# the range goes out of 0 - 18446744073709551615
def test_clu64_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 18446744073709551615"):
        _ = CLU64(2**64-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 18446744073709551615"):
        _ = CLU64(-1)


# ==== RESULTHOLDER
result_holder_clu64 = CLU64(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu64.to_json()
    assert result == "U64"


# ===== CLU128 =====
clu128_value = CLU128(123)


def test_clu128_serialize():
    result = clu128_value.serialize().hex()
    assert result == "017b"


def test_clu128_value():
    result = clu128_value.value()
    assert result == 123


def test_clu128_cl_value():
    result = clu128_value.cl_value()
    assert result == "02000000017b06"


def test_clu128_to_json():
    result = clu128_value.to_json()
    assert result == "U128"


# the range goes out of 0 - 340282366920938463463374607431768211455
def test_clu128_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 340282366920938463463374607431768211455"):
        _ = CLU128(2**128-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 340282366920938463463374607431768211455"):
        _ = CLU128(-1)


# ==== RESULTHOLDER
result_holder_clu128 = CLU128(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu128.to_json()
    assert result == "U128"


# ===== CLU256 =====
clu256_value = CLU256(123)


def test_clu256_serialize():
    result = clu256_value.serialize().hex()
    assert result == "017b"


def test_clu256_value():
    result = clu256_value.value()
    assert result == 123


def test_clu256_cl_value():
    result = clu256_value.cl_value()
    assert result == "02000000017b07"


def test_clu256_to_json():
    result = clu256_value.to_json()
    assert result == "U256"


# the range goes out of 0 - 115792089237316195423570985008687907853269984665640564039457584007913129639935
def test_clu256_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 115792089237316195423570985008687907853269984665640564039457584007913129639935"):
        _ = CLU256(2**256-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 115792089237316195423570985008687907853269984665640564039457584007913129639935"):
        _ = CLU256(-1)


# ==== RESULTHOLDER
result_holder_clu256 = CLU256(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu256.to_json()
    assert result == "U256"


# ===== CLU512 =====
clu512_value = CLU512(123)


def test_clu512_serialize():
    result = clu512_value.serialize().hex()
    assert result == "017b"


def test_clu512_value():
    result = clu512_value.value()
    assert result == 123


def test_clu512_cl_value():
    result = clu512_value.cl_value()
    assert result == "02000000017b08"


def test_clu512_to_json():
    result = clu512_value.to_json()
    assert result == "U512"


# the range goes out of 0 - 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
def test_clu256_out_of_range():
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095"):
        _ = CLU512(2**512-1 + 1)
    with pytest.raises(ValueError, match="The inner value for the number should be 0 - 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095"):
        _ = CLU512(-1)


# ==== RESULTHOLDER
result_holder_clu512 = CLU512(RESULTHOLDER())


def test_result_holder_to_json():
    result = result_holder_clu512.to_json()
    assert result == "U512"
