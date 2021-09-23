def test_affectation_a(v):
    assert v == 8, "tu n'as pas affecté la valeur 8 à la variable a"

def test_affectation_b(v):
    assert v == 7, "tu n'as pas affecté la valeur 7 à la variable b"
    
def test_affectation_toto(v):
    assert v == 15, "tu n'as pas affecté la somme à la variable toto"
    
def test_addition(a, b, toto):
    test_affectation_a(a)
    test_affectation_b(b)
    test_affectation_toto(toto)
    return "les tests ont réussi"

def test_fonction_addition(val):
    assert val == 8 + 7, "le résultat n'est pas bon. Regarde attentivement le code de la cellule précédente !"
    return "les tests ont réussi"