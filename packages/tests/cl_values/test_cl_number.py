"""Tests for CL (Casper) numeric value types.

This module contains test cases for various numeric CL value types including:
- CLBool: Boolean values
- CLI32/CLI64: Signed 32/64-bit integers
- CLU8/CLU32/CLU64/CLU128/CLU256/CLU512: Unsigned integers of various sizes

Each type is tested for:
- Serialization to bytes
- Value retrieval
- CL value representation
- JSON representation
- Range validation
- NoneHolder handling
"""

import pytest

from python_condor import (
    CLI32, CLI64, CLU128, CLU256, CLU32, CLU512, CLU64, CLU8, CLBool, NoneHolder
)

# === CLBool Tests ===


def test_clbool_true_serialization():
    """Test serialization of CLBool True value."""
    clbool_true = CLBool(True)
    result = clbool_true.serialize().hex()
    assert result == "01"


def test_clbool_true_value():
    """Test value retrieval of CLBool True."""
    clbool_true = CLBool(True)
    result = clbool_true.value()
    assert result is True


def test_clbool_true_cl_value():
    """Test CL value representation of CLBool True."""
    clbool_true = CLBool(True)
    result = clbool_true.cl_value()
    assert result == "010000000100"


def test_clbool_true_to_json():
    """Test JSON representation of CLBool True."""
    clbool_true = CLBool(True)
    result = clbool_true.to_json()
    assert result == "Bool"


def test_clbool_invalid_type():
    """Test CLBool rejects non-boolean values."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'str'> for CLBool. Allowed value is <class 'bool'>"):
        _ = CLBool("somethingelse")
    with pytest.raises(TypeError, match="Invalid type of input: <class 'int'> for CLBool. Allowed value is <class 'bool'>"):
        _ = CLBool(1)


def test_clbool_false_serialization():
    """Test serialization of CLBool False value."""
    clbool_false = CLBool(False)
    result = clbool_false.serialize().hex()
    assert result == "00"


def test_clbool_false_value():
    """Test value retrieval of CLBool False."""
    clbool_false = CLBool(False)
    result = clbool_false.value()
    assert result is False


def test_clbool_false_cl_value():
    """Test CL value representation of CLBool False."""
    clbool_false = CLBool(False)
    result = clbool_false.cl_value()
    assert result == "010000000000"


def test_clbool_false_to_json():
    """Test JSON representation of CLBool False."""
    clbool_false = CLBool(False)
    result = clbool_false.to_json()
    assert result == "Bool"


def test_clbool_none_holder():
    """Test CLBool with NoneHolder value."""
    result_holder = CLBool(NoneHolder())
    result = result_holder.to_json()
    assert result == "Bool"


# === CLI32 Tests ===

def test_cli32_serialization():
    """Test serialization of CLI32 value."""
    cli32_value = CLI32(123)
    result = cli32_value.serialize().hex()
    assert result == "7b000000"


def test_cli32_value():
    """Test value retrieval of CLI32."""
    cli32_value = CLI32(123)
    result = cli32_value.value()
    assert result == 123


def test_cli32_cl_value():
    """Test CL value representation of CLI32."""
    cli32_value = CLI32(123)
    result = cli32_value.cl_value()
    assert result == "040000007b00000001"


def test_cli32_to_json():
    """Test JSON representation of CLI32."""
    cli32_value = CLI32(123)
    result = cli32_value.to_json()
    assert result == "I32"


def test_cli32_out_of_range():
    """Test CLI32 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 2147483648 exceeds maximum 2147483647 for CLI32"):
        _ = CLI32(2**31)
    with pytest.raises(ValueError, match="Value -2147483649 below minimum -2147483648 for CLI32"):
        _ = CLI32(-2**31 - 1)


def test_cli32_none_holder():
    """Test CLI32 with NoneHolder value."""
    result_holder = CLI32(NoneHolder())
    result = result_holder.to_json()
    assert result == "I32"


# === CLI64 Tests ===

def test_cli64_serialization():
    """Test serialization of CLI64 value."""
    cli64_value = CLI64(123)
    result = cli64_value.serialize().hex()
    assert result == "7b00000000000000"


def test_cli64_value():
    """Test value retrieval of CLI64."""
    cli64_value = CLI64(123)
    result = cli64_value.value()
    assert result == 123


def test_cli64_cl_value():
    """Test CL value representation of CLI64."""
    cli64_value = CLI64(123)
    result = cli64_value.cl_value()
    assert result == "080000007b0000000000000002"


def test_cli64_to_json():
    """Test JSON representation of CLI64."""
    cli64_value = CLI64(123)
    result = cli64_value.to_json()
    assert result == "I64"


def test_cli64_out_of_range():
    """Test CLI64 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 9223372036854775808 exceeds maximum 9223372036854775807 for CLI64"):
        _ = CLI64(2**63)
    with pytest.raises(ValueError, match="Value -9223372036854775809 below minimum -9223372036854775808 for CLI64"):
        _ = CLI64(-2**63 - 1)


def test_cli64_none_holder():
    """Test CLI64 with NoneHolder value."""
    result_holder = CLI64(NoneHolder())
    result = result_holder.to_json()
    assert result == "I64"


# === CLU8 Tests ===

def test_clu8_serialization():
    """Test serialization of CLU8 value."""
    clu8_value = CLU8(123)
    result = clu8_value.serialize().hex()
    assert result == "7b"


def test_clu8_value():
    """Test value retrieval of CLU8."""
    clu8_value = CLU8(123)
    result = clu8_value.value()
    assert result == 123


def test_clu8_cl_value():
    """Test CL value representation of CLU8."""
    clu8_value = CLU8(123)
    result = clu8_value.cl_value()
    assert result == "010000007b03"


def test_clu8_to_json():
    """Test JSON representation of CLU8."""
    clu8_value = CLU8(123)
    result = clu8_value.to_json()
    assert result == "U8"


def test_clu8_out_of_range():
    """Test CLU8 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 256 exceeds maximum 255 for CLU8"):
        _ = CLU8(256)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU8"):
        _ = CLU8(-1)


def test_clu8_none_holder():
    """Test CLU8 with NoneHolder value."""
    result_holder = CLU8(NoneHolder())
    result = result_holder.to_json()
    assert result == "U8"


# === CLU32 Tests ===

def test_clu32_serialization():
    """Test serialization of CLU32 value."""
    clu32_value = CLU32(123)
    result = clu32_value.serialize().hex()
    assert result == "7b000000"


def test_clu32_value():
    """Test value retrieval of CLU32."""
    clu32_value = CLU32(123)
    result = clu32_value.value()
    assert result == 123


def test_clu32_cl_value():
    """Test CL value representation of CLU32."""
    clu32_value = CLU32(123)
    result = clu32_value.cl_value()
    assert result == "040000007b00000004"


def test_clu32_to_json():
    """Test JSON representation of CLU32."""
    clu32_value = CLU32(123)
    result = clu32_value.to_json()
    assert result == "U32"


def test_clu32_out_of_range():
    """Test CLU32 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 4294967296 exceeds maximum 4294967295 for CLU32"):
        _ = CLU32(2**32)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU32"):
        _ = CLU32(-1)


def test_clu32_none_holder():
    """Test CLU32 with NoneHolder value."""
    result_holder = CLU32(NoneHolder())
    result = result_holder.to_json()
    assert result == "U32"


# === CLU64 Tests ===

def test_clu64_serialization():
    """Test serialization of CLU64 value."""
    clu64_value = CLU64(123)
    result = clu64_value.serialize().hex()
    assert result == "7b00000000000000"


def test_clu64_value():
    """Test value retrieval of CLU64."""
    clu64_value = CLU64(123)
    result = clu64_value.value()
    assert result == 123


def test_clu64_cl_value():
    """Test CL value representation of CLU64."""
    clu64_value = CLU64(123)
    result = clu64_value.cl_value()
    assert result == "080000007b0000000000000005"


def test_clu64_to_json():
    """Test JSON representation of CLU64."""
    clu64_value = CLU64(123)
    result = clu64_value.to_json()
    assert result == "U64"


def test_clu64_out_of_range():
    """Test CLU64 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 18446744073709551616 exceeds maximum 18446744073709551615 for CLU64"):
        _ = CLU64(2**64)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU64"):
        _ = CLU64(-1)


def test_clu64_none_holder():
    """Test CLU64 with NoneHolder value."""
    result_holder = CLU64(NoneHolder())
    result = result_holder.to_json()
    assert result == "U64"


# === CLU128 Tests ===

def test_clu128_serialization():
    """Test serialization of CLU128 value."""
    clu128_value = CLU128(123)
    result = clu128_value.serialize().hex()
    assert result == "017b"


def test_clu128_value():
    """Test value retrieval of CLU128."""
    clu128_value = CLU128(123)
    result = clu128_value.value()
    assert result == 123


def test_clu128_cl_value():
    """Test CL value representation of CLU128."""
    clu128_value = CLU128(123)
    result = clu128_value.cl_value()
    assert result == "02000000017b06"


def test_clu128_to_json():
    """Test JSON representation of CLU128."""
    clu128_value = CLU128(123)
    result = clu128_value.to_json()
    assert result == "U128"


def test_clu128_out_of_range():
    """Test CLU128 rejects values outside valid range."""
    with pytest.raises(ValueError, match="Value 340282366920938463463374607431768211456 exceeds maximum 340282366920938463463374607431768211455 for CLU128"):
        _ = CLU128(2**128)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU128"):
        _ = CLU128(-1)


def test_clu128_none_holder():
    """Test CLU128 with NoneHolder value."""
    result_holder = CLU128(NoneHolder())
    result = result_holder.to_json()
    assert result == "U128"


# === CLU256 Tests ===

def test_clu256_serialization():
    """Test serialization of CLU256 value."""
    clu256_value = CLU256(123)
    result = clu256_value.serialize().hex()
    assert result == "017b"


def test_clu256_value():
    """Test value retrieval of CLU256."""
    clu256_value = CLU256(123)
    result = clu256_value.value()
    assert result == 123


def test_clu256_cl_value():
    """Test CL value representation of CLU256."""
    clu256_value = CLU256(123)
    result = clu256_value.cl_value()
    assert result == "02000000017b07"


def test_clu256_to_json():
    """Test JSON representation of CLU256."""
    clu256_value = CLU256(123)
    result = clu256_value.to_json()
    assert result == "U256"


def test_clu256_out_of_range():
    """Test CLU256 rejects values outside valid range."""
    with pytest.raises(ValueError, match="115792089237316195423570985008687907853269984665640564039457584007913129639936 exceeds maximum 115792089237316195423570985008687907853269984665640564039457584007913129639935 for CLU256"):
        _ = CLU256(2**256)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU256"):
        _ = CLU256(-1)


def test_clu256_none_holder():
    """Test CLU256 with NoneHolder value."""
    result_holder = CLU256(NoneHolder())
    result = result_holder.to_json()
    assert result == "U256"


# === CLU512 Tests ===

def test_clu512_serialization():
    """Test serialization of CLU512 value."""
    clu512_value = CLU512(123)
    result = clu512_value.serialize().hex()
    assert result == "017b"


def test_clu512_value():
    """Test value retrieval of CLU512."""
    clu512_value = CLU512(123)
    result = clu512_value.value()
    assert result == 123


def test_clu512_cl_value():
    """Test CL value representation of CLU512."""
    clu512_value = CLU512(123)
    result = clu512_value.cl_value()
    assert result == "02000000017b08"


def test_clu512_to_json():
    """Test JSON representation of CLU512."""
    clu512_value = CLU512(123)
    result = clu512_value.to_json()
    assert result == "U512"


def test_clu512_out_of_range():
    """Test CLU512 rejects values outside valid range."""
    with pytest.raises(ValueError, match="13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096 exceeds maximum 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095 for CLU512"):
        _ = CLU512(2**512)
    with pytest.raises(ValueError, match="Value -1 below minimum 0 for CLU512"):
        _ = CLU512(-1)


def test_clu512_none_holder():
    """Test CLU512 with NoneHolder value."""
    result_holder = CLU512(NoneHolder())
    result = result_holder.to_json()
    assert result == "U512"
