import pytest
from result import Err, Ok

from python_condor import CLU32, CLU64, CLBool, CLResult, CLTuple2, CLString, CLOption, NoneHolder


# ===== CLResult OK =====

clresult_ok = CLResult(Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
                       Err(CLU32(NoneHolder())), True)


def test_clresult_ok_serialize():
    result = clresult_ok.serialize().hex()
    assert result == "01010500000068656c6c6f7b00000000000000"


def test_clresult_ok_string_value():
    result = clresult_ok.value()
    assert result == {'Ok': ('hello', 123)}


def test_clresult_ok_cl_value():
    result = clresult_ok.cl_value()
    assert result == "1300000001010500000068656c6c6f7b00000000000000100d130a0504"


def test_clresult_ok_to_json():
    result = clresult_ok.to_json()
    assert result == {'Result': {'err': 'U32', 'ok': {
        'Option': {'Tuple2': ['String', 'U64']}}}}


# # ===== CLResult Err =====
clresult_err = CLResult(
    Ok(CLBool(NoneHolder())), Err(CLU32(10)), False)


def test_clresult_err_serialize():
    result = clresult_err.serialize().hex()
    assert result == "000a000000"


def test_clresult_err_string_value():
    result = clresult_err.value()
    assert result == {'Err': 10}


def test_clresult_err_cl_value():
    result = clresult_err.cl_value()
    assert result == "05000000000a000000100004"


def test_clresult_err_to_json():
    result = clresult_err.to_json()
    assert result == {'Result': {'err': 'U32', 'ok': 'Bool'}}
