import numpy as np
import matplotlib.pyplot as plt
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

#ouvre et convertit le fichier ech
ech = np.loadtxt("/Users/claire/Python/IR/sPEEKHyb8H2O205.txt",delimiter="\t",dtype=float)

#affiche tableau ref x et y avec 2 colonnes
print('ech',ech)

#affiche minimum de y de ref
minyech=np.min(ech[:,1])
print('minyech',minyech)

#soustrait min à tous les y de la 2eme colonne
for i in range(0,ech.shape[1]):
    ech[i] = ech[i] - (0,minyech)
print('echb',ech)

#soustrait ref à ech et met ça dans matrice sous
sous = []
sous = ech - ref
sousbis = np.delete(sous,0,axis=1)
souster = np.insert(sousbis,0,ref[:,0],axis=1)
print('soustraction',souster)

#trace ref
plt.subplot(111)
plt.plot(ref[:,0],ref[:,1],'b',label='Spectre référence')

#trace ech
plt.subplot(111)
plt.plot(ech[:,0],ech[:,1],'r',label='Spectre échantillon')

#trace soustraction
plt.subplot(111)
plt.plot(souster[:,0],souster[:,1],'y--',label='Spectre soustraction échantillon-référence')

#Mets tout ce qui est légende des graphs
plt.title('Spectre IR')
plt.xlabel('longueur onde cm-1')
plt.ylabel('Intensité')
plt.legend()
plt.show()
