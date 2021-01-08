# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:55:39 2020

@author: José
"""

# =============================================================================
# Exercice 2
# =============================================================================

def mystere():
    """
    renvoie la somme des 5 premiers entiers
    Returns
    -------
    nombre : int
        la somme des 5 premiers entiers.
    """


def somme(n):
    """
    renvoie la somme des n premiers entiers

    Parameters
    ----------
    n : int

    Returns
    -------
    nombre : int
        la somme des n premiers entiers

    Exemple
    -------
    >>> somme(5)
    15
    """


def somme2(n):
    """
    renvoie la somme des n premiers entiers pairs

    Parameters
    ----------
    n : int

    Returns
    -------
    nombre : int
        la somme des n premiers entiers pairs.

    Exemple
    -------
    >>> somme2(5)
    6
    >>> somme2(6)
    12

    """


def multiples(n):
    """
    affiche les n premiers entiers multiples de 3

    Parameters
    ----------
    n : int

    Returns
    -------
    None.

    """


def somme_inverse(n):
    """
    renvoie la somme de l'inverse des n premiers entiers

    Parameters
    ----------
    n : int

    Returns
    -------
    somme : float
        la somme des 1/i.

    Exemple
    -------
    >>> somme_inverse(2)
    1.5
    >>> round(somme_inverse(3),2)
    1.83
    """




# =============================================================================
# Exercice 3
# =============================================================================
def increment(a, b):
    """
    incrémente la valeur de a tant que a est inférieur à b
    
    Parameters
    ----------
    a : int
    b : int
    
    Returns
    -------
    None
    """
    
    
def increment2(a, b):
    """
    incrémente la valeur de a tant que a est inférieur à b
    
    Parameters
    ----------
    a : int
    b : int
    
    Returns
    -------
    compteur : int
        le nombre de fois où la boucle a été exécutée
        
    Exemple
    -------
    >>> increment2(2, 3)
    1
    >>> increment2(2, 4)
    2
    """

    
    
def impaire(a, b):
    """
    affiche les valeurs impaires de b tant que a est inférieur à b
    
    Parameters
    ----------
    a : int
    b : int
    
    Returns
    -------
    None
    """

    
def impaire2(a, b):
    """
    renvoie le nombre de valeurs impaires de b tant que a est inférieur à b
    
    Parameters
    ----------
    a : int
    b : int
    
    Returns
    -------
    compteur : int
        le nombre de fois où la boucle a été exécutée
        
    Exemple
    -------
    >>> impaire2(2, 4)
    1
    >>> impaire2(2, 5)
    2
    """
    
    
# =============================================================================
# Exercice 4
# =============================================================================

def quotient(x, y):
    """
    renvoie le quotient de la division euclidienne de x par y

    Parameters
    ----------
    x : int
        le dividende.
    y : int
        le diviseur.

    Returns
    -------
    resultat : int
        le quotient de la division de x par y.

    Exemple
    -------
    >>> quotient(0, 2)
    0
    >>> quotient(4, 2)
    2
    >>> quotient(3, 2)
    1
    """


def reste(x, y):
    """
    renvoie le reste de la division euclidienne de x par y

    Parameters
    ----------
    x : int
        le dividende.
    y : int
        le diviseur.

    Returns
    -------
    resultat : int
        le quotient de la division de x par y.

    Exemple
    -------
    >>> reste(0, 2)
    0
    >>> reste(4, 2)
    0
    >>> reste(5, 2)
    1
    """

# =============================================================================
# Exercice 5
# =============================================================================

def syracuse(n):
    """
    renvoie le temps de vol de la suite de Syracuse

    Parameters
    ----------
    n : int

    Returns
    -------
    temps_vol : int
        le nmbre de sauts pour atteindre 1.

    Exemple
    -------
    >>> syracuse(5)
    5

    """



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
