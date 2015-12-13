#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#TP 4 http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_iteration_conditionnelle.html
#TP 4 : Itération conditionnelle

#somme_partielle

import math
import sys        
        
def somme_partielle(n):
    while n > 0:
        i = (-1) * n
        return i   
        
#Tables de multiplication

def imprimer_table(k):
  
    assert(type(k) is int), "k doit être un entier"

    for i in range(1, 11):
        print(k, "×", i, "=", k*i)
        
  for table in range(1, 11):
    imprimer_table(table)

#Suite arithmético-géométrique

# [Q1] 
u_0 = 0
u_1 = 3*u_0+1
u_2 = 3*u_1+1

# [Q2]
def u_terme(n):
    """
    Renvoie la valeur de u_n.
    CU : n ≥ 0
    Exemple:
    >>> u_terme(0)
    0
    >>> u_terme(59)
    7065193045869367252382405533
    """
    assert(type(n) is int and n >= 0), "n doit être un entier positif"

    u = 0
    for i in range(1, n+1):
        u = 3*u+1
    return u


# [Q3]

def atteint(M):
    assert(type(M) is int or type(M) is float), "M doit être un numérique"

    u = 0
    n = 0
    while u <= M:
        n += 1
        u = 3*u+1
    return n
    
#Choisis un nombre

from random import randint
def jeu():
    """
    Lance un jeu de + ou -.
    CU : nombre minimum inférieur au nombre maximum,
    nombre d'essais supérieur à 0
    """
    print("Jeu du + ou -")
    continuer_jeu = True # Cette variable permet de savoir si il faut continuer
    # à demander un nombre ou non.

    # On demande au joueur les valeurs avec lesquels il veut jouer
    minimum = int(input("Entrez le nombre minimum : ")) # Q7
    maximum = int(input("Entrez le nombre maximum : ")) # Q7
    assert(minimum < maximum), "Le nombre minimum doit être inférieur au \
        nombre maximum" # Q7
    maxEssais = int(input("Entrez le nombre d'essais : ")) # Q7
    assert(maxEssais > 0), "Le nombre d'essais doit être supérieur à 0" # Q7
    # minimum = 1 # Pré-Q7
    # maximum = 100 # Pré-Q7
    # maxEssais = 1 # Pré-Q7
    essais = 0 # Comptabilise les essais réalisés
    # J'utilise un autre nom de variable pour être conforme à la règle PEP 3104
    mystere2 = randint(minimum, maximum) # On pioche le nombre mystère
    # print("Nombre à trouver :", mystere2) # Décommenter pour tricher
    while continuer_jeu:
        proposition = int(input("Entrez un nombre entre "+str(minimum)+" et "+\
            str(maximum)+" ("+str(maxEssais - essais)+" essais restants): "))
        if proposition >= minimum and proposition <= maximum: # Si le nombre est
        # en dehors de l'intervalle, on ne fait rien (pas même compter un essai)
        # et on revient à l'affichage du essage
            if proposition == mystere2:
                print("C'est GAGNÉ")
                continuer_jeu = False # On coupe la boucle
            else: # Ce décalage permet, en cas de victoire, de ne pas afficher
            # comme quoi le nombre d'essai est dépassé ni de compter un essai
            # supplémentaire
                essais += 1 # On comptabilise l'essai
                if proposition < mystere2: # Si le nombre est inférieur
                    print("C'est PLUS")
                elif proposition > mystere2: # Si le nombre est supérieur
                    print("C'est MOINS")
                if essais >= maxEssais: # Q6
                    print("Vous avez dépassé le nombre d'essais autorisés") # Q6
                    continuer_jeu = False # Q6
    score = int((7**2 * (maximum - minimum))/(maxEssais*99)-essais) # Q7
    # J'utilise cette méthode de calcul de score car :
    # - Elle donne les mêmes résultat que le jeu décrit dans le sujet pour un
    #     intervalle de [1,100] et un nombre d'essai de 7
    # - Elle est est proportionelle à l'intervalle entre les bornes du choix
    # - Elle est est inversement proportionelle au nombre d'essais donné
    # - Elle me parait relativement équitable
    # - Elle est tronquée pour la lisibilité

    # score = 7 - essais # Pré-Q7
    print("Vous avez marqué", score, "points.")
    
#Recherche de zéro par dichotomie

def f(x):
    """
    Renvoie la valeur x**2-3
    CU : x réel positif
    Exemple :
    >>> f(0)
    -3
    >>> f(42)
    1761
    """
    assert((type(x) is int or type(x) is float) and x >= 0), \
        "x doit être un réel positif"

    return x**2-3

# [Q2] Créez deux variables a et b, puis calculez f(a) et f(b)
a = 0
b = 2

f_a = f(a) # -3
f_b = f(b) # 1

# [Q2] Calculez aussi la longueur de l’intervalle [a,b].
intervalle = b-a

# [Q3] Créez une variable c puis calculez f(c).
c = intervalle/2+a # 1
f_c = f(c) # -2

# [Q3] Doit-on chercher le zéro de f dans l’intervalle ]a,c[ ou dans
# l’intervalle ]c,b[ ?

# f(c) vaut -2, donc 0 ∈ [f(c);f(b)], donc on doit chercher le zéro de f dans
# ]c,b[

# [Q4] Écrivez une fonction zero qui prend un paramètre epsilon
# strictement positif et qui renvoie une approximation du zéro de f à epsilon
# / 2 près.
def zero(epsilon):
    """
    Renvoie une approximation du zéro de f à epsilon/2 près.
    CU : epsilon doit être un réel supérieur à 0
    Exemple :
    >>> zero(0.1)
    1.6875
    >>> zero(0.00001)
    1.7320480346679688
    """
    assert((type(epsilon) is int or type(epsilon) is float) and epsilon >= 0), \
        "epsilon supérieur à 0"

    # Pour être conforme à la règle PEP 3104
    mini = a
    maxi = b

    while maxi - mini >= epsilon:
        milieu = (maxi - mini)/2+mini
        if f(milieu) > 0:
            maxi = milieu
        else:
            mini = milieu
    return milieu

# [Q5] Modifiez votre fonction zero pour qu’elle accepte en paramètres
# n’importe quelle fonction continue strictement monotone et n’importe quel
# intervalle initial contenant le zéro de cette fonction.
def fTest(x): # Fonction fournie pour tester zeroGenrique
    """
    Renvoie la valeur x**3-4
    CU : x réel
    Exemple :
    >>> f(0)
    -3
    >>> f(42)
    1761
    """
    assert((type(x) is int or type(x) is float)), \
        "x doit être un réel"

    return x**3-4

def zeroGenerique(fonction, mini, maxi, epsilon):
    """
    Renvoie une approximation du zéro de la fonction f entre mini et maxi
    à epsilon/2 près.
    CU : fonction E → F continue et monotone avec E,F ⊂ ℝ, mini,maxi ∈ E,
    mini<maxi, epsilon réel supérieur à 0
    Exemple :
    >>> zeroGenerique(fTest, -10, 10, 0.001)
    1.5875244140625
    """
    assert(type(mini) is int or type(mini) is float), "mini doit être un réel"
    assert(type(maxi) is int or type(maxi) is float), "maxi doit être un réel"
    assert(mini < maxi), "mini doit être inférieur à maxi"
    assert((type(epsilon) is int or type(epsilon) is float) and epsilon >= 0), \
        "epsilon doit être un réel supérieur à 0"

    while maxi - mini >= epsilon:
        milieu = (maxi - mini)/2+mini
        if fonction(milieu) > 0:
            maxi = milieu
        else:
            mini = milieu
    return milieu
    
