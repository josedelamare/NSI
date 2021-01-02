# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:40:54 2020

@author: José
"""

# =============================================================================
# Import des modules
# =============================================================================
import doctest

# =============================================================================
# Exercice 3-1
# =============================================================================
def mem(tup, donnee):
    """
    renvoie True si donnee est dans tuple

    Parameters
    ----------
    tup : tuple
        le tuple dans lequel on cherche.
    donnee : TYPE
        l'élément recherché.

    Returns
    -------
    un booléen.

    Exemple
    -------
    >>> mem(('peche', ('pomme', 'poire'), 12.5, -5), 'peche')
    True
    >>> mem(('peche', ('pomme', 'poire'), 12.5, -5), 'pomme')
    False
    """

# =============================================================================
# Exercice 3-2
# =============================================================================
def mem(tup, donnee):
    """
    renvoie True si donnee est dans tuple

    Parameters
    ----------
    tup : tuple
        le tuple dans lequel on cherche.
    donnee : TYPE
        l'élément recherché.

    Returns
    -------
    reponse : bool ou tuple
        False ou (True, indice).

    Exemple
    -------
    >>> mem(('peche', ('pomme', 'poire'), 12.5, -5), 'peche')
    (True, 0)
    >>> mem(('peche', ('pomme', 'poire'), 12.5, -5), 'pomme')
    False
    """

# =============================================================================
# Exercice 4
# =============================================================================
def compte(tup, element):
    """
    renvoie le nombre de fois où element est dans tup

    Parameters
    ----------
    tup : tuple
        le tuple dans lequel on cherche.
    element : TYPE
        l'élément recherché.

    Returns
    -------
    nombre : int
        le nombre de fois où l'élément est présent.

    Exemple
    -------
    >>> compte((3, "manteau", 5.0, "pêche", 3), 3)
    2
    >>> compte((3, "manteau", 5.0, "pêche", 3), "robe")
    0
    """

    return nombre

# =============================================================================
# Exercice 5
# =============================================================================
def division_euclidienne(n1, n2):
    """
    renvoie le quotient et le reste de la division euclidienne de n1 par n2

    Parameters
    ----------
    n1 : int
        le dividende.
    n2 : int
        le diviseur.

    Returns
    -------
    resultat : tuple
        contient le quotient et le reste

    Exemple
    -------
    >>> division_euclidienne(5, 2)
    (2, 1)
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
