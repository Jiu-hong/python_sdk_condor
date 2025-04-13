"""
Tests for PackageHashTarget functionality.

This module contains test cases for the PackageHashTarget class, which represents
package hash targets in Casper transactions. The tests verify:
- Package hash target creation with and without version
- Byte serialization
- JSON serialization
- Input validation for package hash format
"""

import pytest

from python_condor import PackageHashTarget


# Test data setup
RUNTIME = "VmCasperV1"
PACKAGE_HASH = "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56"


def create_test_package_hash_target(version: int = None) -> PackageHashTarget:
    """
    Create a test package hash target with sample data.

    Args:
        version: Optional version number for the package

    Returns:
        PackageHashTarget: A configured test target
    """
    return PackageHashTarget(RUNTIME, PACKAGE_HASH, version)


# Expected test results
EXPECTED_NO_VERSION_BYTES = (
    "0300000000000000000001000100000002003d0000004c00000001030000000000000000000100010000000200210000002200000002cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b5600010000000000000000000100000000"
)

EXPECTED_NO_VERSION_JSON = {
    'target': {
        'Stored': {
            'id': {
                'ByPackageHash': {
                    'addr': PACKAGE_HASH,
                    'version': None
                }
            },
            'runtime': RUNTIME
        }
    }
}

EXPECTED_WITH_VERSION_BYTES = (
    "030000000000000000000100010000000200410000005000000001030000000000000000000100010000000200210000002600000002cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b560101000000010000000000000000000100000000"
)

EXPECTED_WITH_VERSION_JSON = {
    'target': {
        'Stored': {
            'id': {
                'ByPackageHash': {
                    'addr': PACKAGE_HASH,
                    'version': 1
                }
            },
            'runtime': RUNTIME
        }
    }
}


def test_target_no_version_to_bytes():
    """Test byte serialization of package hash target without version."""
    target = create_test_package_hash_target()
    result = target.to_bytes().hex()
    assert result == EXPECTED_NO_VERSION_BYTES


def test_target_no_version_to_json():
    """Test JSON serialization of package hash target without version."""
    target = create_test_package_hash_target()
    result = target.to_json()
    assert result == EXPECTED_NO_VERSION_JSON


def test_target_with_version_to_bytes():
    """Test byte serialization of package hash target with version."""
    target = create_test_package_hash_target(version=1)
    result = target.to_bytes().hex()
    assert result == EXPECTED_WITH_VERSION_BYTES


def test_target_with_version_to_json():
    """Test JSON serialization of package hash target with version."""
    target = create_test_package_hash_target(version=1)
    result = target.to_json()
    assert result == EXPECTED_WITH_VERSION_JSON


def test_package_hash_format_validation():
    """Test validation of package hash format."""
    with pytest.raises(ValueError, match=r"package-hash should only contain alphabet and number\(64 length\)"):
        _ = PackageHashTarget(RUNTIME, "123-0")
