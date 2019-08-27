import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#ouvre et convertit le fichier ref
ref = np.loadtxt("/Users/claire/Python/IR/sPEEKHyb8.txt",delimiter="\t",dtype=float)

#affiche tableau ref x et y avec 2 colonnes
print('ref',ref)

#affiche minimum de y de ref
minyref=np.min(ref[:,1])
print('minyref',minyref)

#soustrait min à tous les y de la 2eme colonne
for i in range(0,ref.shape[1]):
    ref[i] = ref[i] - (0,minyref)
print('refb',ref)

#Sépare les colonnes en x et y
x=ref[:,0]
y=ref[:,1]

#Définit une limite basse pour la détection des pics
I=(np.max(ref[:,1]))/10
print('I',I)

#Fonction de détection des pics (peaks est l'indexation)
peaks, _ = find_peaks(y, height=(I, None))

#Crée un tableau avec tous les pics
pics = x[np.ix_(peaks)]
print('pics',pics)

#Crée un tableau avec tous les y des pics
picsy = y[np.ix_(peaks)]

#trace le spectre et met une croix sur les pics idenfifiés
plt.plot(x,y)
plt.plot(pics, y[peaks], "x")

#Charge la base de donnée
texte = pd.read_excel('/Users/claire/Python/IR/Base.xlsx')

#transforme en array
base = texte.values
print('base',base)

#définit les listes à comparer
borne_inf = base[:,0]
borne_sup = base[:,1]
liaisons = base[:,2]

#Compare les pics trouvé avec la borne inf et sup de la base de données et donne la liste des liaisons trouvées
#Problème renvoie seulement 1 liaison
for j in range(0,pics.shape[0]):
    if borne_inf[j] < pics[j] < borne_sup[j]:
        print ('liaisons', liaisons[j])
        #ne marche pas :
        #plt.text(pics[j], picsy[j], liaisons[j])

print('liaisons', liaisons[j])



plt.show()
