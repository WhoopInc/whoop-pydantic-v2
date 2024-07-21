from unittest.mock import patch

import pytest
from packaging.version import parse as parse_version

import whoop_pydantic_v2
from whoop_pydantic_v2.version import version_info, version_short


def test_version_info():
    version_info_fields = [
        'whoop_pydantic_v2 version',
        'whoop_pydantic_v2-core version',
        'whoop_pydantic_v2-core build',
        'install path',
        'python version',
        'platform',
        'related packages',
        'commit',
    ]

    s = version_info()
    assert all([f'{field}:' in s for field in version_info_fields])
    assert s.count('\n') == 7


def test_standard_version():
    v = parse_version(whoop_pydantic_v2.VERSION)
    assert str(v) == whoop_pydantic_v2.VERSION


def test_version_attribute_is_present():
    assert hasattr(whoop_pydantic_v2, '__version__')


def test_version_attribute_is_a_string():
    assert isinstance(whoop_pydantic_v2.__version__, str)


@pytest.mark.parametrize('version,expected', (('2.1', '2.1'), ('2.1.0', '2.1')))
def test_version_short(version, expected):
    with patch('whoop_pydantic_v2.version.VERSION', version):
        assert version_short() == expected
