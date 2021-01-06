# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:39:14 2021

@author: José
"""

# =============================================================================
# Recherche d'une racine carré par dichotomie
# =============================================================================

def racine_dichotomie(nombre, epsilon):
    """
    Recherche d'une racine carré par dichotomie

    Parameters
    ----------
    nombre : flot
        le nombre dont on cherche la racine carré.
    epsilon : float
        la précision.

    Returns
    -------
    racine : float
        la racine carré du nombre.

    Exemple
    -------
    >>> round(racine_dichotomie(1, 1e-3), 2)
    1.0
    >>> round(racine_dichotomie(4, 1e-3), 2)
    2.0
    """

    return racine

# =============================================================================
# Recherche d'une racine carré par la méthode de Héron
# =============================================================================

def racine_heron(nombre, epsilon):
    """
    Recherche d'une racine carré par la méthode de Heron

    Parameters
    ----------
    nombre : flot
        le nombre dont on cherche la racine carré.
    epsilon : float
        la précision.

    Returns
    -------
    racine : float
        la racine carré du nombre.

    Exemple
    -------
    >>> round(racine_heron(1, 1e-3), 2)
    1
    >>> round(racine_heron(4, 1e-3), 2)
    2.0
    """

    return racine

# =============================================================================
# Test des fonctions
# =============================================================================

if __name__ == "__main__":
    import doctest
    doctest.testmod()
