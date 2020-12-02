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

def factorielle(n):
    resultat = 1
    if n >= 1:
        for i in range(1, n+1):
            resultat = resultat * i
    return resultat

def somme_diff_quotient_reste(n1,n2):
    somme = n1 + n2
    difference = n1 - n2
    quotient = n1//n2
    reste = n1%n2
    return somme, difference, quotient, reste

def est_bisextile(a):
    if a%400 == 0:
        reponse = True
    elif a%4 == 0 and a%100 != 0:
        reponse = True
    else:
        reponse = False
    return reponse

def maximum(a,b,c):
    maxi = a
    if b > maxi:
        maxi = b
    if c > maxi:
        maxi = c
    return maxi
        

########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
inputs_factorielle = [
    Args(1),
    Args(2),
    Args(5),
    Args(10),
    Args(15),
    Args(150)
]

inputs_somme = [
    Args(1, 1),
    Args(1, 2),
    Args(2, 1),
    Args(10, 5),
    Args(15, 7),
    Args(15, 4)
]

inputs_bisextile = [
    Args(2020),
    Args(2008),
    Args(1900),
    Args(2000)
]

inputs_maximum = [
    Args(1, 2, 3),
    Args(3, 2, 1),
    Args(3, 1, 2)
]


########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_factorielle = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    factorielle,
    # the inputs
    inputs_factorielle,
    result_renderer=PPrintRenderer(width=20),
)

exo_somme = ExerciseFunction(
    somme_diff_quotient_reste,
    inputs_somme,
    result_renderer=PPrintRenderer(width=20),
)

exo_est_bisextile = ExerciseFunction(
    est_bisextile,
    inputs_bisextile,
    result_renderer=PPrintRenderer(width=20),
)

exo_maximum = ExerciseFunction(
    maximum,
    inputs_maximum,
    result_renderer=PPrintRenderer(width=20),
)


