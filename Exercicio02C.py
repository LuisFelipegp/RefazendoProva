import pytest

def string_invert(s):

    str_invertida = ""
    for c in s[::-1]:
        str_invertida += c
    return str_invertida


def test_string_invert_com_mais_de_um_caractere():
    
    s = "olá"
    expected = "álo"
    actual = string_invert(s)
    assert expected == actual