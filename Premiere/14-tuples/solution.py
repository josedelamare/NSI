# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020
@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


########## step 1
# You need to define the 'correct' function
# i.e. one that would be accepted as valid for the problem

def ajout_tete(t, elt):
    """ajout d'un élément en première position d'un tuple
    Entrées : t (un tuple) et elt (l'élément à ajouter)
    Sortie : new_tup : un tuple
    """
    new_tup = (elt,)
    longueur = len(t)
    for i in range (0, longueur, 1):
        new_tup = new_tup + (t[i],)
    return new_tup

def ajout_position(t, elt, i):
    """ajout d'un élément en dernière position d'un tuple
    Entrées : t (un tuple), elt (l'élément à ajouter) et i (la position)
    Sortie : new_tup : un tuple
    """
    new_tup = ()
    longueur = len(t)
    for j in range (0, i, 1):
        new_tup = new_tup + (t[j],)
    new_tup = new_tup + (elt,)
    for j in range (i, longueur, 1):
        new_tup = new_tup + (t[j],)
    return new_tup

def supp_queue(t):
    """suppression d'un élément en dernière position d'un tuple
    Entrées : t (un tuple)
    Sortie : new_tup : un tuple
    """    
    ##--Indiquez le code Python, puis cliquez sur Run--##    
    new_tup = ()
    longueur = len(t)
    for j in range (0, longueur-1, 1):
        new_tup = new_tup + (t[j],)
    return new_tup

def supp_tete(t):
    """suppression d'un élément en première position d'un tuple
    Entrées : t (un tuple)
    Sortie : new_tup : un tuple
    """    
    ##--Indiquez le code Python, puis cliquez sur Run--##    
    new_tup = ()
    longueur = len(t)
    for j in range (1, longueur, 1):
        new_tup = new_tup + (t[j],)
    return new_tup

def supp_position(t, i):
    """suppression d'un élément en position i d'un tuple
    Entrées : t (un tuple) et i (la position)
    Sortie : new_tup : un tuple
    """
    new_tup = ()
    longueur = len(t)
    for j in range (0, i, 1):
        new_tup = new_tup + (t[j],)
    for j in range (i+1, longueur, 1):
        new_tup = new_tup + (t[j],)
    return new_tup
    

########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
t = ('foo', 'bier', 'baz', 7, ('bar', 'bot'), 29)
inputs_ajout_tete = [
    Args(t, 2),
    Args(t, 'toto'),
    Args(t, (2, 'toto')),
    Args(t, (2, (3, 'toto')))
]

inputs_ajout_position = [
    Args(t, 2, 1),
    Args(t, 'toto', 3),
    Args(t, (2, 'toto'), 0),
    Args(t, (2, (3, 'toto')), 4)
]

inputs_supp_queue = [
    Args(t)]

inputs_supp_tete = [
    Args(t)
]

inputs_supp_position = [
    Args(t, 2),
    Args(t, 3),
    Args(t, 0),
    Args(t, 4)
]



########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_ajout_tete = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    ajout_tete,
    # the inputs
    inputs_ajout_tete,
    result_renderer=PPrintRenderer(width=20),
)

exo_ajout_position = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    ajout_position,
    # the inputs
    inputs_ajout_position,
    result_renderer=PPrintRenderer(width=20),
)

exo_supp_tete = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    supp_tete,
    # the inputs
    inputs_supp_tete,
    result_renderer=PPrintRenderer(width=20),
)

exo_supp_queue = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    supp_queue,
    # the inputs
    inputs_supp_queue,
    result_renderer=PPrintRenderer(width=20),
)

exo_supp_position = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    supp_position,
    # the inputs
    inputs_supp_position,
    result_renderer=PPrintRenderer(width=20),
)


