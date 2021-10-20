import doctest

def test_factorielle(func,var):
    assert func(12) == 479001600, "la fonction ne semble pas fonctionner pour nombre = 12"
    assert var == 479001600, "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')
    
def test_somme_entiers(func, var):
    assert func(12) == 66, "la fonction ne semble pas fonctionner pour n = 12"
    assert var == 66, "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')
    
def test_somme_carres(func, var):
    assert func(12) == 506, "la fonction ne semble pas fonctionner pour n = 12"
    assert var == 506, "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')