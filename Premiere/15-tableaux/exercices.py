# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:01:19 2019

@author: José
"""
# =============================================================================
# Import des modules
# =============================================================================


# =============================================================================
# Exercice 3-1
# =============================================================================
def multiples_1(n):
    """
    renvoie un tableau contenant les 10 premiers multiples de n

    Parameters
    ----------
    n : int
        le nombre de valeurs du tableau.

    Returns
    -------
    t : list
        un tableau contenant les multiples de 5.

    Exemple
    -------
    >>> multiples_1(1)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> multiples_1(5)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    """



# =============================================================================
# Exercice 3-2
# =============================================================================
def multiples_2(n):
    """
    renvoie un tableau contenant les multiples de n inférieurs à 100

    Parameters
    ----------
    n : int
        le nombre de valeurs du tableau.

    Returns
    -------
    t : list
        un tableau contenant les multiples de n.

    Exemple
    -------
    >>> multiples_2(20)
    [20, 40, 60, 80]
    """



# =============================================================================
# Exercice 3-3
# =============================================================================
def produit(nombres,n) :
    """
    renvoie un tableau contenant les produits des valeurs de nombres par n

    Parameters
    ----------
    n : int
        le nombre de valeurs du tableau.
    nombres : list
        le tableau de nombres

    Returns
    -------
    t : list
        un tableau contenant les produits de nombres par n.

    Exemple
    -------
    >>> produit([4, 5, 6], 2)
    [8, 10, 12]
    """


# =============================================================================
# Exercice 4
# =============================================================================
def monome(x) :
    resultat = 3*x + 2
    return resultat

def map(f,t) :
    """
    renvoie la liste des f(x) où x est un élément de t

    Parameters
    ----------
    f : function
        la fonction.
    t : list
        la liste d'antécédents.

    Returns
    -------
    tableau : list
        la liste d'images de t par f.

    Exemple
    -------
    >>> map(monome, [1, 2, 3, 4])
    [5, 8, 11, 14]
    """


# =============================================================================
# Test de l'ensemble des fonctions
# =============================================================================

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)