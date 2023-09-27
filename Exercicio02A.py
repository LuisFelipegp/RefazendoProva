import pytest

def string_invert(s):
    str_invertida = ""
    for c in s[::-1]:
        str_invertida += c
    return str_invertida


def test_string_invert_vazia():
    s = ""
    expected = ""
    actual = string_invert(s)
    assert expected == actual


if __name__ == "__main__":
    pytest.main()