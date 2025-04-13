"""
Tests for PackageNameTarget functionality.

This module contains test cases for the PackageNameTarget class, which represents
package name targets in Casper transactions. The tests verify:
- Package name target creation with and without version
- Byte serialization
- JSON serialization
"""

from python_condor import PackageNameTarget


# Test data setup
RUNTIME = "VmCasperV1"
PACKAGE_NAME = "my_hash"


def create_test_package_target(version: int = None) -> PackageNameTarget:
    """
    Create a test package name target with sample data.

    Args:
        version: Optional version number for the package

    Returns:
        PackageNameTarget: A configured test target
    """
    return PackageNameTarget(RUNTIME, PACKAGE_NAME, version)


# Expected test results
EXPECTED_NO_VERSION_BYTES = (
    "0300000000000000000001000100000002002800000037000000010300000000000000000001000100000002000c0000000d00000003070000006d795f6861736800010000000000000000000100000000"
)

EXPECTED_NO_VERSION_JSON = {
    'target': {
        'Stored': {
            'id': {
                'ByPackageName': {
                    'name': PACKAGE_NAME,
                    'version': None
                }
            },
            'runtime': RUNTIME
        }
    }
}

EXPECTED_WITH_VERSION_BYTES = (
    "0300000000000000000001000100000002002c0000003b000000010300000000000000000001000100000002000c0000001100000003070000006d795f686173680101000000010000000000000000000100000000"
)

EXPECTED_WITH_VERSION_JSON = {
    'target': {
        'Stored': {
            'id': {
                'ByPackageName': {
                    'name': PACKAGE_NAME,
                    'version': 1
                }
            },
            'runtime': RUNTIME
        }
    }
}


def test_target_no_version_to_bytes():
    """Test byte serialization of package target without version."""
    target = create_test_package_target()
    result = target.to_bytes().hex()
    assert result == EXPECTED_NO_VERSION_BYTES


def test_target_no_version_to_json():
    """Test JSON serialization of package target without version."""
    target = create_test_package_target()
    result = target.to_json()
    assert result == EXPECTED_NO_VERSION_JSON


def test_target_with_version_to_bytes():
    """Test byte serialization of package target with version."""
    target = create_test_package_target(version=1)
    result = target.to_bytes().hex()
    assert result == EXPECTED_WITH_VERSION_BYTES


def test_target_with_version_to_json():
    """Test JSON serialization of package target with version."""
    target = create_test_package_target(version=1)
    result = target.to_json()
    assert result == EXPECTED_WITH_VERSION_JSON
