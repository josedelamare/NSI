# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020
@author: José
"""

def test_identification(func):
    # on teste le type de la première valeur
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert type(result[0]) is int
    except :
        return "l'identifiant n'est pas un entier"
    
    # on teste le type des deux autres valeurs
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert type(result[1]) is str and type(result[2]) is str
    except :
        return "le nom et le prénom de sont pas des chaînes de caractères"
    
    # on teste l'exemple
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert result == [213615200, 'BESNIER', 'JEAN']
    except :
        return "l'exemple ne passe pas les test"
    
    # on teste le séparateur
    try :        
        chaine = '213615200,BESNIER,JEAN'
        result = func(chaine)
        return "la fonction ne tient pas compte du séparateur"
    except ValueError:
        pass
    
    # on teste la longueur de chaque élément de la chaine
    try :        
        chaine = '2;B;J'
        result = func(chaine)
        assert result == [2, 'B', 'J']
    except ValueError:
        return "la fonction plante si la longueur de chaque "
    
    # on teste la présence du prénon
    try :        
        chaine = '213615200;BESNIER;'
        result = func(chaine)
        assert result == [213615200, 'BESNIER', '']
    except :
        return "la fonction ne tient pas compte de l'absence du prénom"
    
    # on teste la présence du nom
    try :        
        chaine = '213615200;;JEAN'
        result = func(chaine)
        assert result == [213615200, '', 'JEAN']
    except :
        return "la fonction ne tient pas compte de l'absence du nom"
    
    return "Bravo ! tous les tests ont réussi"



def test_creation(func):
    # on teste si l'objet créé est un dictionnaire
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert type(result) is dict
    except :
        return "l'objet créé n'est pas un dictionnaire"
    
    # on teste si la clé est un entier
    chaine = '213615200;BESNIER;JEAN'
    result = func(chaine)
    for cle in result.keys():            
        try :
            assert type(cle) is int
        except :
            return "la clé n'est pas un entier"
    
    # on teste si la clé est bonne
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert 213615200 in result.keys()
    except :
        return "la clé n'est pas la bonne."
    
    # on teste si la valeur est une chaîne de caractères
    chaine = '213615200;BESNIER;JEAN'
    result = func(chaine)
    for val in result.values():            
        try :
            assert type(val) is str
        except :
            return "la valeur n'est pas une chaîne de caractères"
    
    # on teste si la valeur est bonne
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert 'JEAN BESNIER' in result.values()
    except :
        return "la valeur n'est pas la bonne."
    
    # on teste l'exemple
    try :
        chaine = '213615200;BESNIER;JEAN'
        result = func(chaine)
        assert result == {213615200: 'JEAN BESNIER'}
    except :
        return "l'exemple ne passe pas les test"
    
    # on teste le séparateur
    try :        
        chaine = '213615200,BESNIER,JEAN'
        result = func(chaine)
        return "la fonction ne tient pas compte du séparateur"
    except ValueError:
        pass
    
    # on teste la présence du prénon
    try :        
        chaine = '213615200;BESNIER;'
        result = func(chaine)
        assert result == {213615200: ' BESNIER'}
    except :
        return "la fonction ne tient pas compte de l'absence du prénom"
    
    # on teste la présence du nom
    try :        
        chaine = '213615200;;JEAN'
        result = func(chaine)
        assert result == {213615200: 'JEAN '}
    except :
        return "la fonction ne tient pas compte de l'absence du nom"
    
    return "Bravo ! tous les tests ont réussi"



def test_ajout(func):    
    # on teste si la clé est un entier
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    for cle in dico.keys():            
        try :
            assert type(cle) is int
        except :
            return "la clé n'est pas un entier"
    
    # on teste si la clé est bonne
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    try :
        assert 213615200 in dico.keys()
    except :
        return "la clé n'est pas la bonne."
    
    # on teste si la valeur est une chaîne de caractères
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    for val in dico.values():            
        try :
            assert type(val) is str
        except :
            return "la valeur n'est pas une chaîne de caractères"
    
    # on teste si la valeur est bonne
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    try :
        assert 'JEAN BESNIER' in dico.values()
    except :
        return "la valeur n'est pas la bonne."
    
    # on teste l'exemple
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    try :
        assert 213615200 in dico.keys() and 'JEAN BESNIER' in dico.values()
    except :
        return "l'exemple ne passe pas les test"
    
    # on regarde si le dictionnaire est modifié
    chaine = '213615200;BESNIER;JEAN'
    dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
    func(dico, chaine)
    try :
        assert len(dico) == 3
    except :
        return "le dictionnaire original n'est pas modifié"
    
    # on teste le séparateur
    try :        
        chaine = '213615200,BESNIER,JEAN'
        func(dico, chaine)
        return "la fonction ne tient pas compte du séparateur"
    except ValueError:
        pass
    
    # on teste la présence du prénon
    try :        
        chaine = '213615200;BESNIER;'
        dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
        func(dico, chaine)
        assert ' BESNIER' in dico.values()
    except :
        return "la fonction ne tient pas compte de l'absence du prénom"
    
    # on teste la présence du nom
    try :        
        chaine = '213615200;;JEAN'
        dico = {298394849: 'JEAN BONO', 2349432: 'JEFF AILIDIOT'}
        func(dico, chaine)
        assert 'JEAN ' in dico.values()
    except :
        return "la fonction ne tient pas compte de l'absence du nom"
    
    return "Bravo ! tous les tests ont réussi"
    