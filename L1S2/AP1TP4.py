# SHCHERBAKOVA Iuliia
# GPE 45 Info/EEA
# Evaluation empirique des tris

display = __name__ == '__main__'
def partie(name):
    if display:
        print('\n☕', 'Partie', name, '☕')

partie(": Prérequis")        

def comp(x, y):
    """
    CU : aucune
    """

    global counter
    counter = counter + 1
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

partie(": Préliminaires")

def liste_croissante(n):
    return list(range(n))

def liste_decroissante(n):
    rev = list(range(n))
    rev.reverse()
    print(rev)

import random
from random import shuffle

def liste_alea(n):
    rev = list(range(n))
    random.shuffle(rev)
    print(rev)

partie(": prise en main de Gnuplot")
print('*')
print("Déduisez-en le rôle de with lines")
print("La commande 'with lines' nous permmet d'ajouter des \
lignes entre des points.")
print('*')

partie(": la méthode 'format'")

print("##########")
for n in range(0,101):
    print('{0}; {1};'.format(n,(n * (n+1)) // 2))

partie(": lancer une commande système")

print(">>> import os")
print(">>> os.system('lowriter')")
print('*')
print("Que renvoie la fonction lors de la fermeture du traitement de texte ?")
print('*')
print("1")
print('*')
print("system(...)\
system(command) -> exit_status")

partie(": le module timeit")
import timeit
print("*")
print(">>> timeit.timeit(stmt='sqrt(2)')")
print("NameError: name 'sqrt' is not defined")
print('*')
print(">>> timeit.timeit(stmt='sqrt(2)', setup='from math import sqrt')")
print("0.17186516559810627")
print('*')
print(">>> timeit.timeit(stmt='sqrt(2)', setup='from math import \
sqrt',number=5000)")
print("0.0008480562650277079")
print('*')
print(">>> timeit.timeit(stmt='sqrt(2) ; sqrt(3)', \
setup='from math import sqrt')")
print("0.36995232330076533")
print('*')

partie(": cas du tri par selection")

print("---------------------------------------")
print("Comme le resultat est trop long, \
vous pouvez trouver cette partie dans le fichier liste_alea.py")
print("---------------------------------------")
print('*')
print("J'ai le résultat 38.10457192021419")
print('*')



 



