# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:10:30 2020

@author: José
"""


def dichotomie_indice(liste, val):
    """renvoie l'indice de val dans liste ou -1 si val est absent
    Entrée
        val : la valeur recherchée, un entier
        liste : une liste d'entiers triés par ordre croissant
    Sortie
        l'indice de position, un entier ou -1

    Exemple d'exécution
    >>> dichotomie_indice([1,2,3],2)
    1
    >>> dichotomie_indice([1,2,3],1)
    0
    >>> dichotomie_indice([1,2,3],4)
    -1
    """



def dichotomie_indice_2(liste, val):
    """renvoie l'indice de val dans liste ou -1 si val est absent
    Entrée
        val : la valeur recherchée, un entier
        liste : une liste d'entiers triés par ordre croissant
    Sortie
        l'indice de position, un entier ou -1

    Exemple d'exécution
    >>> dichotomie_indice_2([1,2,3],2)
    (1, 1)
    >>> dichotomie_indice_2([1,2,3],1)
    (0, 2)
    >>> dichotomie_indice_2([1,2,3],4)
    (-1, 3)
    """



def recherche_racine(a, b, epsilon):
    """renvoie la valeur pour laquelle f(racine) = 0
    Entrée :
        a, la borne inférieure, un entier
        b, la borne supérieure, un entier
        epsilon, la précision, un réel
    Sortie :
        racine, la valeur qui annule la fonction, un réel
        iteration , le nombre d'itérations, un entier
    """



def resolution_equation(a, b, epsilon, k):
    """renvoie la valeur pour laquelle f(racine) = 0
    Entrée :
        a, la borne inférieure, un entier
        b, la borne supérieure, un entier
        epsilon, la précision, un réel
    Sortie :
        racine, la valeur qui annule la fonction, un réel
        iteration , le nombre d'itérations, un entier
    """



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
