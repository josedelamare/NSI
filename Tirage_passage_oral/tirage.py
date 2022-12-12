# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:55:26 2021

@author: José
"""

# =============================================================================
# Import des modules
# =============================================================================
import csv
from random import randint

# =============================================================================
# Constantes
# =============================================================================
POINT_PASSAGE = 10 #nombre de points acquis lors de chaque passage à l'oral
ECART_MAX_PASSAGE = 2 #écart maximal du nombre de passage entre celui qui est le plus passé et le moins passé
COEFF_PASSAGE = 0.5
COEFF_NOTES = 0.5
MAX_JOKERS = 3 #nombre maximum de Jokers que l'on peut utiliser

# =============================================================================
# Ouverture du fichier
# =============================================================================
def ouverture(fichier):
    """
    ouverture du fichier et écriture des informations dans un dictionnaire

    Parameters
    ----------
    fichier : str
        le nom du fichier.

    Returns
    -------
    table : list
        Une liste de dictionnaires

    """
    with open(fichier) as mon_fichier:
        table = list(csv. DictReader(mon_fichier, delimiter=';'))
    for ligne in table:
        ligne["notes"] = ligne["notes"].split(',')

    #postconditions
    assert type(table) is list
    for elt in table:
        assert type(elt) is dict

    return table

# =============================================================================
# Calcul du nombre de passages effectués
# =============================================================================
def nb_passages(ma_table):
    """
    renvoie un dictionnaire :
        clé : le nom
        valeur : le nombre de notes

    Parameters
    ----------
    ma_table : list
        une liste de dictionnaires.

    Returns
    -------
    d : dict
        clé : le nom
        valeur : le nombre de notes

    """

    #préconditions
    assert type(ma_table) is list
    for elt in ma_table:
        assert type(elt) is dict

    d = {}
    for dico in ma_table:
        if dico["notes"] == ['']:
            d[dico["nom"]] = 0
        else:
            nb = 0
            for note in dico["notes"]:
                if note != 'Joker':
                    nb = nb + 1
            d[dico["nom"]] = nb

    #postconditions
    assert type(d) is dict
    for cle, valeur in d.items():
        assert type(cle) is str
        assert type(valeur) is int

    return d

# =============================================================================
# Calcul de la moyenne des notes
# =============================================================================
def moyenne_notes(ma_table):
    """
    renvoie un dictionnaire :
        clé : le nom
        valeur : la moyenne des notes

    Parameters
    ----------
    ma_table : list
        une liste de dictionnaires.

    Returns
    -------
    d : dict
        clé : le nom
        valeur : le nombre de notes

    """

    #préconditions
    assert type(ma_table) is list
    for elt in ma_table:
        assert type(elt) is dict

    d = {}
    for dico in ma_table:
        if dico["notes"] == ['']:
            d[dico["nom"]] = None
        else:
            nb = 0
            somme = 0
            for note in dico["notes"]:
                if note != 'Joker':
                    nb = nb + 1
                    somme = somme + float(note)
            d[dico["nom"]] = somme/nb

    #postconditions
    assert type(d) is dict
    for cle, valeur in d.items():
        assert type(cle) is str
        assert type(valeur) is float or valeur is None

    return d

# =============================================================================
# Détermination du nombre de passages le plus grand
# =============================================================================
def passage_max(mon_dico):
    """
    renvoie le nombre maximal de passages des élèves de la classe

    Parameters
    ----------
    mon_dico : dict
        clé : le nom
        valeur : le nombre de passages à l'oral.

    Returns
    -------
    nb : int
        le nombre de passages de l'élève le plus interrogé.

    """

    #préconditions
    assert type(mon_dico) is dict
    for cle, valeur in mon_dico.items():
        assert type(cle) is str
        assert type(valeur) is int
        assert valeur >= 0

    nb = 0
    for valeur in mon_dico.values():
        if valeur > nb:
            nb = valeur

    #postconditions
    assert type(nb) is int
    assert nb >= 0

    return nb

# =============================================================================
# Pour les élèves qui ne sont jamais passés à l'oral
# =============================================================================
def premier_passage(mon_dico):
    '''
    renvoie les élèves qui ne sont jamais passés à l'oral

    Parameters
    ----------
    mon_dico : dict
        clé : le nom
        valeur : le nombre de passages à l'oral.

    Returns
    -------
    table : list
        le nom des élèves qui ne sont jamais passés à l'oral.

    '''

    #préconditions
    assert type(mon_dico) is dict
    for cle, valeur in mon_dico.items():
        assert type(cle) is str
        assert type(valeur) is int
        assert valeur >= 0

    table = []
    for cle,valeur in mon_dico.items():
        if valeur == 0:
            table = table + [cle]

    #postconditions
    assert type(table) is list
    for elt in table:
        assert type(elt) is str or elt is None

    return table

# =============================================================================
# Calcul du score de chaque élève
# =============================================================================
def calcul_score(nb_notes, moyenne):
    '''
    renvoie un dictionnaire :
        clé : le nom
        valeur : le score de chaque élève

    Parameters
    ----------
    nb_notes : dict
        clé : le nom
        valeur : le score de chaque élève.
    moyenne : dict
        clé : le nom
        valeur : la moyenne de chaque élève.

    Returns
    -------
    d : dict
        clé : le nom
        valeur : le score de chaque élève

    '''

    #préconditions
    assert type(nb_notes) is dict
    assert len(nb_notes) != 0
    all([isinstance(cle, str) for cle in nb_notes.keys()])
    all([isinstance(valeur, float) for valeur in nb_notes.values()])

    assert type(moyenne) is dict
    assert len(moyenne) != 0
    all([isinstance(cle, str) for cle in moyenne.keys()])
    all([isinstance(valeur, float) for valeur in moyenne.values()])

    assert len(moyenne) == len(nb_notes)

    #code
    d = {}
    for cle in nb_notes.keys():
        if nb_notes[cle] != 0:
            d[cle] = (nb_notes[cle]*COEFF_NOTES*POINT_PASSAGE + moyenne[cle]*COEFF_PASSAGE)/(COEFF_NOTES + COEFF_PASSAGE)
        else:
            d[cle] = 0.0

    #postconditions
    assert type(d) is dict
    assert len(d) != 0
    assert all([isinstance(cle, str) for cle in d.keys()])
    assert all([isinstance(valeur, float) for valeur in d.values()])

    return d

# =============================================================================
# Sélection des élèves ayant un score particulier
# =============================================================================
def ajout_eleves(mon_dico, val):
    '''
    renvoie une liste des élèves dont le score est égal à val

    Parameters
    ----------
    mon_dico : dict
        clé : le nom
        valeur : le score de chaque élève.
    val : float
        le score à chercher.

    Returns
    -------
    table : list
        la liste des élèves dont le score est val.

    '''
    #précondition
    assert type(mon_dico) is dict
    assert all([isinstance(cle, str) for cle in mon_dico.keys()])
    assert all([isinstance(valeur, float) for valeur in mon_dico.values()])

    #code
    table = []
    for cle, valeur in mon_dico.items():
        if valeur == val:
            table = table + [cle]

    #postconditions
    assert type(table) is list
    assert all([isinstance(elt, str) for elt in table])

    return table

# =============================================================================
# Sélection des élèves qui sont le moins passés
# =============================================================================
def ajout_ecart(mon_dico, maxi):
    '''
    renvoie une liste des élèves dont le nombre de passage est inférieur à
    ECART_MAX_PASSAGE de celui qui est le plus passé

    Parameters
    ----------
    mon_dico : dict
        clé : le nom
        valeur : le score de chaque élève.

    maxi : int
        le nombre maximal de passages

    Returns
    -------
    table : list
        la liste des élèves dont le score est val.

    '''
    #précondition
    assert type(mon_dico) is dict
    assert all([isinstance(cle, str) for cle in mon_dico.keys()])
    assert all([isinstance(valeur, int) for valeur in mon_dico.values()])

    #code
    table = []
    for cle, valeur in mon_dico.items():
        if maxi - valeur > ECART_MAX_PASSAGE:
            table = table + [cle]

    #postconditions
    assert type(table) is list
    assert all([isinstance(elt, str) for elt in table])

    return table

# =============================================================================
# Tirage au sort de l'élève élu
# =============================================================================
def tirage(ma_liste):
    '''
    renvoie l'élément tiré au sort dans la liste

    Parameters
    ----------
    ma_liste : list
        une liste de noms.

    Returns
    -------
    elt : str
        un nom tiré au hasard dans la liste.

    '''
    #préconditions
    assert len(ma_liste) != 0
    assert all([isinstance(elt, str) for elt in ma_liste])

    #code
    i = randint(0, len(ma_liste)-1)
    elt = ma_liste[i]

    #postconditions
    assert type(elt) is str

    return elt

# =============================================================================
# Identification du nombre de Jokers d'un élève
# =============================================================================
def nb_jokers(ma_table, mon_eleve):
    '''
    renvoie le nombre de Jokers déjà utilisés par un élève

    Parameters
    ----------
    ma_table : list
        une liste de dictionnaires.
    mon_eleve : str
        le nom de l'élève.

    Returns
    -------
    nb : int
        le nombre de Jokers déjà utilisés.

    '''

    #préconditions
    assert type(ma_table) is list
    assert all([isinstance(elt, dict) for elt in ma_table])

    #code
    nb = 0
    for elt in ma_table:
        if elt['nom'] == mon_eleve:
            nb = elt['notes'].count('Joker')

    #postconditions
    assert type(nb) is int
    assert nb >= 0

    return nb

# =============================================================================
# Recherche si l'élève a utilisé un Joker à l'interrogation précédente
# =============================================================================
def joker_precedent(ma_table, mon_eleve):
    '''
    renvoie True si l'élève a utilisé un Joker lors de l'interrogation précédente

    Parameters
    ----------
    ma_table : list
        une liste de dictionnaires.
    mon_eleve : str
        le nom de l'élève.

    Returns
    -------
    reponse : bool

    '''

    #préconditions
    assert type(ma_table) is list
    assert all([isinstance(elt, dict) for elt in ma_table])

    #code
    reponse = False
    for elt in ma_table:
        if elt['nom'] == mon_eleve:
            if elt['notes'][-1] == 'Joker':
                reponse = True

    #postconditions
    assert type(reponse) is bool

    return reponse

# =============================================================================
# Programme principal
# =============================================================================
table_eleves = ouverture("notes.csv")
nombre_de_notes = nb_passages(table_eleves)
moyenne_des_notes = moyenne_notes(table_eleves)
nb_passage_max = passage_max(nombre_de_notes)
score_eleve = calcul_score(nombre_de_notes, moyenne_des_notes)

# Pour identifier les élèves qui ne sont pas encore passés
liste_eleves_eligibles = premier_passage(nombre_de_notes)

# S'il y a moins de 5 élèves qui ne sont pas passés, on ajoute ceux qui sont passés le moins de fois
if len(liste_eleves_eligibles) < 5:
    liste_ajouter = ajout_ecart(nombre_de_notes, nb_passage_max)
    for eleve in liste_ajouter:
        if eleve not in liste_eleves_eligibles:
            liste_eleves_eligibles = liste_eleves_eligibles + [eleve]

# S'il y a moins de 5 élèves qui ne sont pas passés, on ajoute les plus faibles
liste_scores = sorted(list(score_eleve.values()), reverse=True)
if liste_scores[-1] == 0.0:
    del liste_scores[-1]
while len(liste_eleves_eligibles) < 5:
    liste_ajouter = ajout_eleves(score_eleve, liste_scores[-1])
    for eleve in liste_ajouter:
        if eleve not in liste_eleves_eligibles:
            liste_eleves_eligibles = liste_eleves_eligibles + [eleve]
    del liste_scores[-1]

# tirage au sort de l'élève et suppression de la liste des élèves éligibles
reponse = 'O'
while reponse == 'O' and len(liste_eleves_eligibles) != 0:
    # eleve_oral = tirage(liste_eleves_eligibles)
    eleve_oral = liste_eleves_eligibles[0]
    print(f"l'élève tiré au sort est {eleve_oral}")
    liste_eleves_eligibles.remove(eleve_oral)

    nb_jokers_utilises = nb_jokers(table_eleves, eleve_oral)
    if nb_jokers_utilises != 0:
        print(f'Cet élève a déjà utilisé {nb_jokers_utilises} Jokers')

    if joker_precedent(table_eleves, eleve_oral):
        print("Cet élève a déjà utilisé 1 Joker à l'interrogation précédente")
        print("Il ne peut donc pas refuser cette interrogation.")

    reponse = input('Voulez-vous faire un nouveau tirage au sort ?').capitalize()
    if len(liste_eleves_eligibles) == 0:
        print("il n'y a plus d'élèves dans la liste. Relancez l'application.")


