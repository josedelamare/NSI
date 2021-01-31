# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020
@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
from random import randint


# les constantes
MON_TABLEAU_INITIAL = ['manger', 'chanter', 'dessiner', 'aspirer']
MON_TABLEAU_TETE = ['commencer', 'manger', 'chanter', 'dessiner', 'aspirer']
MON_TABLEAU_QUEUE = ['manger', 'chanter', 'dessiner', 'aspirer', 'commencer']
MON_TABLEAU_MILIEU = ['manger', 'chanter', 'commencer', 'dessiner', 'aspirer']
MON_TABLEAU_SUPP_TETE = ['chanter', 'dessiner', 'aspirer']
MON_TABLEAU_SUPP_QUEUE = ['manger', 'chanter', 'dessiner']
MON_TABLEAU_SUPP_TETE = ['chanter', 'dessiner', 'aspirer']
MON_TABLEAU_SUPP_MILIEU = ['manger', 'dessiner', 'aspirer']

def exo_ajout_tete_example(tab, elt):
    """ajoute elt en tête de tab"""
    return [elt] + tab

def exo_ajout_tete_correction(tab):
    """verification de l'ajout en tête dans un tableau"""
    assert MON_TABLEAU_TETE == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_ajout_queue_example(tab, elt):
    """ajoute elt en queue de tab"""
    return tab + [elt]

def exo_ajout_queue_correction(tab):
    """verification de l'ajout en queue dans un tableau"""
    assert MON_TABLEAU_QUEUE == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_ajout_milieu_example(tab, elt, n):
    """ajoute elt en milieu de tab"""
    return tab[:n] + [elt] + tab[n:]

def exo_ajout_milieu_correction(tab):
    """verification de l'ajout en milieur dans un tableau"""
    assert MON_TABLEAU_MILIEU == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_supp_tete_example(tab):
    """supprime en tête de tab"""
    return tab[1:]

def exo_supp_tete_correction(tab):
    """verification de la suppression en tête dans un tableau"""
    assert MON_TABLEAU_SUPP_TETE == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"

def exo_supp_queue_example(tab):
    """supprime en queue de tab"""
    return tab[:-1]

def exo_supp_queue_correction(tab):
    """verification de la suppression en queue dans un tableau"""
    assert MON_TABLEAU_SUPP_QUEUE == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_supp_milieu_example(tab, pos):
    """supprime en milieu de tab"""
    return tab[:pos] + tab[pos+1:]

def exo_supp_milieu_correction(tab):
    """verification de la suppression en milieu dans un tableau"""
    assert MON_TABLEAU_SUPP_MILIEU == tab, "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_remplir_1_example(tab, elt):
    """remplir un tableau contenant n fois elt"""
    return len(tab)*[elt]

def exo_remplir_1_correction(tab):
    """verification du remplissage d'un tableau"""
    assert tab == 4*['toto'], "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_multiplication_1_example(k):
    """renvoie les 10 premiers éléments de la table de pultiplication de *k*"""
    return [i*k for i in range(1, 11,1)]

def exo_multiplication_1_correction(tab):
    """verification de la table de multiplication"""
    assert tab == exo_multiplication_1_example(13), "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

def exo_multiplication_2_example(n, k):
    """renvoie les n premier éléments de la table de pultiplication de *k*"""
    return [i*k for i in range(1, n+1,1)]

def exo_multiplication_2_correction(tab):
    """verification de la table de multiplication"""
    assert tab == exo_multiplication_2_example(12, 13), "le tableau t n'est pas correct. Utilisez l'instruction print(t) pour voir le contenu du tableau. Corrigez votre erreur et recommencez"
    return "Je crois que vous avez bien travaillé. Utilisez l'instruction print(t) pour voir le contenu du tableau"

