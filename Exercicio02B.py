import pytest

def string_invert(s):
    str_invertida = ""
    for c in s[::-1]:
        if c != " ":
            str_invertida += c
    return str_invertida

def test_string_invert_com_um_caractere():
    s = "a"
    expected = "a"
    actual = string_invert(s)
    assert expected == actual