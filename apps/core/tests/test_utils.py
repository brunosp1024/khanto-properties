import pytest
from apps.core.utils.functions_utils import generate_random_code


def test_generate_random_code_default_length():
    code = generate_random_code()
    assert len(code) == 8

def test_generate_random_code_custom_length():
    code = generate_random_code(length=12)
    assert len(code) == 12
