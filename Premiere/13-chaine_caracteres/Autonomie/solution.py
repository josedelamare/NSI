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

def ajout_queue(c, car):
    """ajout d'un élément en dernière position d'un tuple
    Entrées : c (une chaîne de caractère) et car (le caractère à ajouter)
    Sortie : new_chaine : une chaîne de caractère
    """
    new_chaine = ""
    longueur = len(c)
    for i in range (0, longueur, 1):
        new_chaine = new_chaine + c[i]
    new_chaine = new_chaine + car
    return new_chaine

def longueur(chaine):
    """renvoie le nombre d'éléments dans la chaîne de caractères"""
    
    longueur = len(chaine)
    return longueur
    
def debut_chaine(chaine):
    """renvoie la chaine sans le dernier caractère"""
    
    copie = ''
    for i in range(0, len(chaine)-1, 1):
        copie = copie + chaine[i]
    return copie
    
def fin_chaine(chaine):
    """renvoie la chaine sans le premier caractère"""
    
    copie = ''
    for i in range(1, len(chaine), 1):
        copie = copie + chaine[i]
    return copie
    

def milieu_chaine(chaine):
    """renvoie la chaine sans le premier ni le dernier caractère"""
    
    copie = ''
    for i in range(1, len(chaine)-1, 1):
        copie = copie + chaine[i]
    return copie

def saut_chaine(chaine):
    """renvoie la chaine en prenant un caractère sur deux"""
    
    copie = ''
    for i in range(0, len(chaine), 2):
        copie = copie + chaine[i]
    return copie

def copie_chaine(chaine):
    """renvoie une copie de la chaîne de caractères"""
    
    copie = ''
    for i in range(0, len(chaine), 1):
        copie = copie + chaine[i]
    return copie

def debut_n_chaine(chaine, n):
    """renvoie les n premiers éléments de la chaîne de caractères"""
    
    copie = ''
    for i in range(0, n, 1):
        copie = copie + chaine[i]
    return copie
    

def fin_n_chaine(chaine, n):
    """renvoie les n derniers éléments de la chaîne de caractères"""
    
    copie = ''
    for i in range(len(chaine) - n, len(chaine), 1):
        copie = copie + chaine[i]
    return copie
    
def milieu_n_chaine(chaine, n1, n2):
    """renvoie la chaîne sans les n1 premiers caractères et sans les n2 premiers caractères"""
    
    copie = ''
    for i in range(n1, len(chaine)- n2, 1):
        copie = copie + chaine[i]
    return copie
    

########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
inputs_ajout_queue = [
    Args("toto", "a"),
    Args("mamie", "a"),
    Args("laitière", "a"),
    Args("anticonstitutionnelement", "a"),
    Args("élastique", "a")
]

inputs_longueur = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]

inputs_copie_chaine = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]


inputs_saut_chaine = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]

inputs_debut_chaine = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]

inputs_debut_n_chaine = [
    Args("toto",2),
    Args("mamie",2),
    Args("laitière",3),
    Args("anticonstitutionnelement",5),
    Args("élastique",5)
]

inputs_fin_chaine = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]

inputs_fin_n_chaine = [
    Args("toto",2),
    Args("mamie",2),
    Args("laitière",3),
    Args("anticonstitutionnelement",5),
    Args("élastique",5)
]

inputs_milieu_chaine = [
    Args("toto"),
    Args("mamie"),
    Args("laitière"),
    Args("anticonstitutionnelement"),
    Args("élastique")
]

inputs_milieu_n_chaine = [
    Args("toto",1,2),
    Args("mamie",1,2),
    Args("laitière",1,3),
    Args("anticonstitutionnelement",3,5),
    Args("élastique",2,3)
]

########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_ajout_queue = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    ajout_queue,
    # the inputs
    inputs_ajout_queue,
    result_renderer=PPrintRenderer(width=20),
)
exo_longueur = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    longueur,
    # the inputs
    inputs_longueur,
    result_renderer=PPrintRenderer(width=20),
)

exo_copie_chaine = ExerciseFunction(
    copie_chaine,
    inputs_copie_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_saut_chaine = ExerciseFunction(
    saut_chaine,
    inputs_saut_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_debut_chaine = ExerciseFunction(
    debut_chaine,
    inputs_debut_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_debut_n_chaine = ExerciseFunction(
    debut_n_chaine,
    inputs_debut_n_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_fin_chaine = ExerciseFunction(
    fin_chaine,
    inputs_fin_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_fin_n_chaine = ExerciseFunction(
    fin_n_chaine,
    inputs_fin_n_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_milieu_chaine = ExerciseFunction(
    milieu_chaine,
    inputs_milieu_chaine,
    result_renderer=PPrintRenderer(width=20),
)

exo_milieu_n_chaine = ExerciseFunction(
    milieu_n_chaine,
    inputs_milieu_n_chaine,
    result_renderer=PPrintRenderer(width=20),
)



# tests supplémentaires
def test_ajout_queue(func,var):
    assert func("mot", "s"), "la fonction ne semble pas fonctionner pour la chaîne mot"
    assert var == "mots", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_saut_chaine(func,var):
    assert func("mot"), "la fonction ne semble pas fonctionner pour la chaîne mot"
    assert var == "mt", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_debut_chaine(func,var):
    assert func("mot"), "la fonction ne semble pas fonctionner pour la chaîne mot"
    assert var == "mo", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_fin_chaine(func,var):
    assert func("mot"), "la fonction ne semble pas fonctionner pour la chaîne mot"
    assert var == "ot", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_milieu_chaine(func,var):
    assert func("mot"), "la fonction ne semble pas fonctionner pour la chaîne mot"
    assert var == "o", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_debut_n_chaine(func,var):
    assert func("barbapapa", 5), "la fonction ne semble pas fonctionner pour la chaîne barbapapa"
    assert var == "barba", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

def test_fin_n_chaine(func,var):
    assert func("barbapapa", 5), "la fonction ne semble pas fonctionner pour la chaîne barbapapa"
    assert var == "apapa", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')
    
def test_milieu_n_chaine(func,var):
    assert func("barbapapa", 3, 2), "la fonction ne semble pas fonctionner pour la chaîne barbapapa"
    assert var == "bapa", "la variable toto n'a pas été utilisée"
    print('tous les tests ont réussi')

