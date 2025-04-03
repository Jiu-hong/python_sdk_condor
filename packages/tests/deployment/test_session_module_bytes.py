from python_condor import SessionModuleBytes, CLU256, CLString


# ===== SessionModuleBytes =====
module_bytes = "01234567"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
session_module_bytes = SessionModuleBytes(
    module_bytes, runtime_args)


def test_session_module_bytes_to_bytes():
    result = session_module_bytes.to_bytes().hex()
    assert result == "00040000000123456702000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"


def test_session_module_bytes_to_json():
    result = session_module_bytes.to_json()
    assert result == {'session': {'ModuleBytes': {'module_bytes': '01234567', 'args': [
        ('arg1', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('arg2', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]}}}
