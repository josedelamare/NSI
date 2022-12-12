# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020

@author: José
"""

import inspect
from IPython.display import HTML

def test(candidate, values, test_type=False):
    # get _correction function
    fonction = candidate.__name__
    good=globals()[fonction+"_correction"]
    # check parametres
    sgood = inspect.signature(good)
    nbParamGood = len(sgood.parameters)
    scand = inspect.signature(candidate)
    nbParamCandidate = len(scand.parameters)
    if nbParamGood != nbParamCandidate:
        return("Erreur ! Votre fonction attend {nbc} variables au lieu de {nbg}".format(nbg=nbParamGood, nbc=nbParamCandidate))

    # Build table
    code = """<table><thead><tr>
          <th>{param}</th>
          <th>{f}{param}<br/> attendu</th>
          <th>{f}{param}<br/> calculé</th>
          <th>Test</th>
        </tr></thead><tbody>""".format(f=fonction, param=scand)

    # Test return values from function and function_correction
    # Build row
    row = """<tr style='background-color:{color}'>
          <td> {x} </td>
          <td> {good} </td>
          <td><b>{candidate}</b></td>
          <td> {check}</td></td>"""
    if nbParamGood > 1:
        for x in values:
            if good(*x) is candidate(*x) if test_type else good(*x) == candidate(*x):
                color, check = '#beffb5', '✅'
            else:
                color, check = '#ffb5b5', '�