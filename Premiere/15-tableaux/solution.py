# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020
@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
from random import randint


########## step 1
# You need to define the 'correct' function
# i.e. one that would be accepted as valid for the problem

def ajout_queue(t, element):
    """renvoie un tableau contenant element ajouté en queue de t"""
    new_tab = (len(t)+1)*[0]
    for i in range(0, len(t), 1):
        new_tab[i] = t[i]
    new_tab[-1] = element
    return new_tab

def ajout_tete(t, element):
    """renvoie un tableau contenant element ajouté en queue de t"""
    new_tab = (len(t)+1)*[0]
    new_tab[0] = element
    for i in range(0, len(t), 1):
        new_tab[i+1] = t[i]
    return new_tab

def miroir(tab):
    """renvoie un tableau dont les éléments sont inversés par rapport à tab - le premier devient le dernier
    Entrées : tab (un tableau)
    Sortie : new_tab (un tableau)
    """  
    new_tab = len(tab)*[0]
    for i in range(0, len(tab), 1):
        new_tab[len(tab)- 1 - i] = tab[i]
    return new_tab

def aleatoire(n, a, b):
    """renvoie un tableau de n éléments, dont les éléments sont tirés aléatoirement entre a et b
    Entrées : n, a, b (des entiers)
    Sortie : tab (un tableau)
    """  
    tab = n*[0]
    for i in range(0, n, 1):
        tab[i] = randint(a,b)
    return tab

def croissant(n, a, b):
    """renvoie un tableau de n éléments, dont les éléments sont croissants
    Entrées : n, a, b (des entiers)
    Sortie : tab (un tableau)
    """  
    tab = n*[0]
    for i in range(0, n, 1):
        tab[i] = tab[i-1] + randint(a,b)
    return tab
    
    

########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#

inputs_creation = [
    Args(2, 1, 10),
    Args(5, 1, 10),
    Args(1, 1, 10)
]

inputs_ajout = [
    Args([1, 2], 3),
    Args(["toto", "tata"], "titi"),
    Args([0], 1)
]

inputs_miroir = [
    Args([1, 2]),
    Args(["toto", "tata"]),
    Args([0]),
    Args(["anticonstitutionnellement"]),
    Args(["élastique", "ceinture", "bretelles"])
]


########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#

exo_aleatoire = ExerciseFunction(
    aleatoire,
    inputs_creation,
    result_renderer=PPrintRenderer(width=50),
)


exo_croissant = ExerciseFunction(
    croissant,
    inputs_creation,
    result_renderer=PPrintRenderer(width=50),
)

exo_ajout_queue = ExerciseFunction(
    ajout_queue,
    inputs_ajout,
    result_renderer=PPrintRenderer(width=50),
)

exo_ajout_tete = ExerciseFunction(
    ajout_tete,
    inputs_ajout,
    result_renderer=PPrintRenderer(width=50),
)

exo_miroir= ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    miroir,
    # the inputs
    inputs_miroir,
    result_renderer=PPrintRenderer(width=50),
)


