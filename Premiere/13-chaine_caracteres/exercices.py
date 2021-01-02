# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:03:23 2020

@author: José
"""

def radical(chaine):
    """
    renvoie le radical d'un verbe du premier graoupe

    Parameters
    ----------
    chaine : str
        un verbe du premier groupe.

    Returns
    -------
    nouvelle_chaine : str
        le radical du verbe.

    Exemples
    --------
    >>> radical('chanter')
    'chant'
    """


def conjugaison(chaine):


def distance_hamming(chaine1, chaine2):
    """
    renvoie la distance de Hamming entre les deux chaines

    Parameters
    ----------
    chaine1 : str
    chaine2 : str
        les deux chaînes de caractères.

    Returns
    -------
    distance : int
        la distance de Hamming.

    Exemples
    --------
    >>> distance_hamming("JAPON", "SAVON")
    2
    """
    assert len(chaine1) == len(chaine2), "les deux chaînes doivent avoir le même nombre de caractères"


def verlan(chaine):
    """
    renvoie la chaine inversée

    Parameters
    ----------
    chaine : str
        une chaine de caractères.

    Returns
    -------
    nouvelle_chaine : str
        la chaine de caractères inversée.

    Exemples
    --------
    >>> verlan("bob")
    'bob'
    >>> verlan("SALUT")
    'TULAS'


    """



def palindrome(chaine):
    """
    renvoie True si la chaine est un palindrome

    Parameters
    ----------
    chaine : str
        la chaine de caractères.

    Returns
    -------
    bool

    Exemples
    --------
    >>> palindrome("bob")
    True
    >>> palindrome("baba")
    False

    """



def cesar(texte, decalage):
    """
    Code un texte en utilisant le chiffrement de Cesar

    Parameters
    ----------
    texte : str
        le texte à coder.
    decalage : int
        le décalage de Cesar.

    Returns
    -------
    nouveau_texte : str
        le message codé.

    Exemples
    --------
    >>> cesar("HELLO", 3)
    'KHOOR'

    """



def cesar2(texte, decalage):
    """
    Code un texte en utilisant le chiffrement de Cesar ET TENANT COMPTE DES ESPACES

    Parameters
    ----------
    texte : str
        le texte à coder.
    decalage : int
        le décalage de Cesar.

    Returns
    -------
    nouveau_texte : str
        le message codé.

    Exemples
    --------
    >>> cesar2("HELLO LE MONDE", 3)
    'KHOOR OH PRQGH'

    """


# =============================================================================
# Test des fonctions
# =============================================================================

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)