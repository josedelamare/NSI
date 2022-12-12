import matplotlib.pyplot as plt
#On note les différentes valeurs du temps (en secondes)
t = [...]

#On note les différentes valeurs de y (en m)
y = [...]

#On definit les listes que l'on va créer
V, tg, Ec, Em, Ep= [], [], [], [], []

# dans une boucle, on parcourt la liste de t et y pour calculer les differentes valeurs de v, Ec, Ep, Em
for i in range(0, len(y)-1):
    Vi = (y[i+1] - y[i])/(t[i+1] - t[i])
    Eci = 1/2 * 0.045 * Vi**2
    Epi = ...
    Emi = ...
    
    # On stocke chaque valeur dans les listes
    V.append(Vi)
    Ec.append(Eci)
    Ep.append(Epi)
    Em.append(Emi)
    tg.append(t[i])
    
# on efface la fenêtre
plt.clf()

#On trace les trois courbes d'energie
plt.plot(tg, Ec, 'or', tg, Ep, 'ob', tg, Em, 'og')

# On ajoute un titre pour chaque axe et pour le graphique
plt.xlabel("temps t (en s)")
plt.ylabel("Energie (en J)")
plt.show()
plt.close()