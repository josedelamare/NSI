import doctest


def test_equation_droite():
    return doctest.run_docstring_examples(equation_droite, globals(), verbose = True)

def test_carre(var):
    #assert aire_carre(9) == 81, "le résultat de la fonction n'est pas bon"
    assert var == 81, "tu n'as pas affecté le résultat de la fonction à la variable mon_carre"
    return "les tests ont réussi"