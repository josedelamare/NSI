# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:03:23 2020

@author: José
"""

# =============================================================================
# Exercice 1
# =============================================================================

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
    """affiche la conjugaison d'un verbe"""

# =============================================================================
# Exercice 2
# =============================================================================

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



def est_paronyme(chaine1, chaine2):
    """
    renvoie True si les deux chaines sont des paronymes (s'ils diffèrent par une lettre')

    Parameters
    ----------
    chaine1 : str
    chaine2 : str
        les deux chaînes de caractères.

    Returns
    -------
    bool

    Exemples
    --------
    >>> est_paronyme("JAPON", "SAVON")
    False
    >>> est_paronyme("collusion", "collision")
    True
    """
    assert len(chaine1) == len(chaine2), "les deux chaînes doivent avoir le même nombre de caractères"


# =============================================================================
# Exercice 3
# =============================================================================
def modification(chaine, car, n):
    """
    renvoie une chaine de caractères dont seule la n-ième lettre de chaine a été modifiée

    Parameters
    ----------
    chaine : str
        la chaine de caractères à modifier.
    car : str
        la lettre à ajouter.
    n : int
        l'indice de la lettre à ajouter.

    Returns
    -------
    new_chaine : str
        la chaine de caractères modifiée.

    Exemples
    --------
    >>> modification('trac', 'u', 2)
    'truc'
    >>> modification("collusion", "i", 4)
    'collision'

    """



# =============================================================================
# Exercice 4
# =============================================================================
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


# =============================================================================
# Exercice 5
# =============================================================================
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
