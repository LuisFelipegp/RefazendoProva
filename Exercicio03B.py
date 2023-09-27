def contarCaracteres(s):
    
    return len(s)

def test_contarCaracteres():
    
    s = "Live long & prosper"
    resultado = contarCaracteres(s)
    assert resultado == 19

if __name__ == "__main__":
    pytest.main()