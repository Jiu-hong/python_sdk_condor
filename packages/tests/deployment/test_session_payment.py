"""
Tests for SessionPayment functionality.

This module contains test cases for the SessionPayment class, which represents
payment sessions in Casper transactions. The tests verify:
- Payment session creation with amount
- Byte serialization
- JSON serialization
"""

from python_condor import SessionPayment


# Test data setup
PAYMENT_AMOUNT = 123456


def create_test_session_payment() -> SessionPayment:
    """
    Create a test session payment with sample data.

    Returns:
        SessionPayment: A configured test payment session
    """
    return SessionPayment(PAYMENT_AMOUNT)


# Expected test results
EXPECTED_BYTES = "00000000000100000006000000616d6f756e74040000000340e20108"

EXPECTED_JSON = {
    'payment': {
        'ModuleBytes': {
            'module_bytes': '',
            'args': [
                ('amount', {
                    'cl_type': 'U512',
                    'bytes': '0340e201',
                    'parsed': PAYMENT_AMOUNT
                })
            ]
        }
    }
}


def test_session_payment_to_bytes():
    """
    Test byte serialization of a session payment.

    Verifies that the session payment correctly serializes to the expected byte format.
    """
    session_payment = create_test_session_payment()
    result = session_payment.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_payment_to_json():
    """
    Test JSON serialization of a session payment.

    Verifies that the session payment correctly serializes to the expected JSON structure.
    """
    session_payment = create_test_session_payment()
    result = session_payment.to_json()
    assert result == EXPECTED_JSON
