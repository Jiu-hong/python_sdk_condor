from python_condor import SessionPayment, CLU256, CLString


# ===== SessionPayment =====

runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
session_payment = SessionPayment(123456)


def test_session_payment_to_bytes():
    result = session_payment.to_bytes().hex()
    assert result == "00000000000100000006000000616d6f756e74040000000340e20108"


def test_session_payment_to_json():
    result = session_payment.to_json()
    assert result == {'payment': {'ModuleBytes': {'module_bytes': '', 'args': [
        ('amount', {'cl_type': 'U512', 'bytes': '0340e201', 'parsed': 123456})]}}}
