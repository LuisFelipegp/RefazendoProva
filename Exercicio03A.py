def contarCaracteres(s):
    """Conta o número de caracteres em uma string, incluindo espaços em branco."""
    count = 0
    for c in s:
        if c.isspace():
            count += 1
        else:
            count += 1
    return count

def test_contarCaracteres():
    """Verifica se a função contarCaracteres retorna o número correto de caracteres, incluindo espaços em branco."""
    s = "Live long & prosper"
    resultado = contarCaracteres(s)
    assert resultado == 19