from .start import soma
import pytest


def test_soma():
    """Testing soma."""
    result = soma(3, 5)
    assert result == 8


def test_sub():
    """Testing sub."""
    pytest.skip("ToDo")


def test_div():
    """Testing div."""
    pytest.skip("ToDo")


def test_mul():
    """Testing mul."""
    pytest.skip("ToDo")
