# Iuliia SHCHERBAKOVA ---  SESI 53 --- 2015/16
# TP2 http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_donnees_expressions.html

#CONVERSION CELSIUS FAHRENHEIT

==================================================================PRINT=======================================================================

C = 20
F = 9/5*C + 32
print('Une température de 20 °C correspond à une température de 68.0 F.')

F2 = 75
C2 = 5/9 * (F - 32)
print('ne température de 75 F correspond à une température de 23.88888888888889 °C.')


============================================================= FAHRENHEIT -> CELSIUS===========================================================


import sys
import time #je vais utiliser ça pour /time.sleep()/

def fahrenheit_en_celsius():
    '''
Vous pouvez faire la conversion Fahrenheit en Celsius avec cette fonction
    '''
celsius = float(input('Saisissez la témperature Celsius: '))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degrés Celsius sont egaux à %0.1f degrés Fahrenheit' %(celsius,fahrenheit))    

time.sleep(10) #suspendre l'exécution du thread courant pour le nombre de secondes donné

print("end")  



==============================================================CELSIUS -> FAHRENHEIT======================================================


import sys
import time

def celsius_en_fahrenheit():
    '''
Vous pouvez faire la conversion Celsius en Fahrenheit avec cette fonction
    '''

fahrenheit = float(input('Saisissez la témperature Fahrenheit: '))

celsius = (fahrenheit - 32) / 1.8
print('%0.1f degrés Fahrenheit sont égaux à %0.1f degrés Celsius' %(fahrenheit,celsius))

time.sleep(10) #suspendre l'exécution du thread courant pour le nombre de secondes donné

print("end")

==============================================================CELSIUS <-> FAHRENHEIT======================================================



import sys
import time #nous allons utiliser cette 

def fahrenheit_en_celsius():
    '''
Vous pouvez faire la conversion Fahrenheit en Celsius avec cette fonction
    '''
celsius = float(input('Saisissez la témperature Celsius: '))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degrés Celsius sont egaux à %0.1f degrés Fahrenheit' %(celsius,fahrenheit))    

time.sleep(2) #suspendre l'exécution du thread courant pour le nombre de secondes donné

print("end")
 
def celsius_en_fahrenheit():
    '''
Vous pouvez faire la conversion Celsius en Fahrenheit avec cette fonction
    '''

fahrenheit = float(input('Saisissez la témperature Fahrenheit: '))

celsius = (fahrenheit - 32) / 1.8
print('%0.1f degrés Fahrenheit sont égaux à %0.1f degrés Celsius' %(fahrenheit,celsius))

time.sleep(10) #suspendre l'exécution du thread courant pour le nombre de secondes donné

print("end")
----------------------------------------------------------------------------------------------------------------------------------------------

#cette fonction est bien réciproque
#fahrenheit = (celsius * 1.8) + 32
#celsius = (fahrenheit - 32) / 1.8

import time
from datetime import datetime 

#référence 1er janvier 1900

ref_an = 1900
ref_mois = 1
ref_jour = 1

nbre_sec_jour = 86400 #on peut considérer qu’une année comprend 365,2425 jours en moyenne
nbre_sec_an = 31556952
nbre_sec_mois = 2629746

#aujourd'hui 27 septembre 2015

aujourdhui_an = 2015
aujourdhui_mois = 9
aujourdhui_jour = 27

#une expression donnant le nombre moyen de secondes écoulées entre la date de référence à 0h00 et la date d’aujourd’hui à 0h00
#(2014-1900) * 365,2425 + (8 * 30,875) + 27 où 30,875 c'est le nombre de jours entre janvier 2015 et aout 2015 en moyenne.
# ça nous donne: 41911,645 jours
# 3621166128 seconds

#AGE EN SECONDES

================================================================AGE EN SECONDES================================================================

from datetime import datetime
import time

print("Je suis née le 2 juillet 1996")

time.sleep(1)

print("Donc...")

time.sleep(2)

delta =(datetime.now() - datetime(1996, 2, 7))
print ("J'ai %d jours et %d seconds" % (delta.days, delta.seconds))

time.sleep(2)

print("La date de naissance de mon ami c'est le 10 août 1991")

time.sleep(1)

print("Donc...")

time.sleep(2)

delta = datetime.now() - datetime(1991, 10, 8)
print ("Il a %d jours et %d seconds" % (delta.days, delta.seconds))

time.sleep(10)

#DEBUT DU DEVELOPPEMENT EN FRACTION CONTINUE D'UN REEL

=====================================================================Q1 ET Q2===================================================================

# Q1
# import math
# math.floor()

# Q2

# exempe: calculer les nombres x, y, z, a0, a1 et a3 avec la fonction /floor/

# on prends la valeur de x = 14.58
# donc floor(x) = a0 = 14
# la difference entre 14.58 et 14 -> [0.58]

# y c'est un nomre inverse de 0.58 donc y = 1/ 0.58
# y = 1/ 0.58 = 1.73 (la difference [0.73] est comprise entre 0 et 1 -> TRUE)

# a1 = floor(y) = 1

# z c'est un nombre inverse de 0.73 donc z = 1/ 0.73
# z = 1.37 (la difference [0.37] est comprise entre 0 et 1 -> TRUE)

# a2 = float(z) = 1

=======================================================================CODE Q2==================================================================

import math
import sys
from math import floor
import time

def afficher_debut():
    '''
avec cette fontion vous pouvez trouver des valeurs de x,y,z et a,a1,a2
    '''

x = float(input('Saisissez le nombre rationel x [ex.: 65.45 ou 10.01 ... : '))
a = floor(x)
print('donc a = %0.1f' %a)

time.sleep(1)

print('Maintenant il  faut calculer y,par definition y = 1/(x-a)')
time.sleep(1)
y = (x-a) ** -1
a1 = floor(y)
print('donc a1 = %0.1f' %a1)

time.sleep(1)

#TAILLE D'UN ENTIER EN BASE 10

=============================================================FONCTIONS /math.log/ et /math.floor/==============================================

import math
math.log10(x)

>>> import math
>>> math.floor(14.78)
14
>>> import math
>>> math.floor(67.1)
67


=================================================================FONCTION TAILLE================================================================

from math import *
import math
import sys

def taille(n):
    if n > 0:
        True
    else:
        print('False')
            
while True:
    n = float(input('Saisissez le nombre positif: '))
    while n > 0:
        print (math.floor(n))

#ça ne marche pas... je sais pas pourquoi mais c'est impossible à calculer /math.floor()/ pour variable n. :(


================================================================LA TAILLE DE 2^100==============================================================

>>> import math
>>> 2 ** 100
1267650600228229401496703205376

>>> len('1267650600228229401496703205376')
>>> 31

========================================================DEMONSTRATION DE LA FONCTION /floor/ (NOMBRES NEGATIFS)=================================

import time

print('Demonstration de fonction /math.floor/ avec des nombres negatifs')
time.sleep(2)
print('Voici un exempe de fonction /floor/')
time.sleep(2)
print('...')
print('...')
print('...')
print('...')
print('...')
print('8/7 == floor(8.0/7.0) == 1 //nombre positif//')
print('8/-7 == floor(8.0/-7.0) == -2 //nombre negatif//')
print('...')
print('...')
print('...')
print('...')
print('...')

#cette fonction retourne l'entier le plus proche, inférieur ou égal au réel passé en paramètre.

time.sleep(2)
print('On peut calculer que 8/7 = 1.15 et 8/-7 = -1.15')
time.sleep(2)
print('...')
print('...')
print('La fonction /floor/ retourne la valeur inférieur ou égal du réel saisi.')
print('...')
print('...')
time.sleep(2)
print('Donc pour 8/7 ça sera 1 et pour 8/-7 ça sera -2')

time.sleep(60)

# Q1
from math import log10

# Q2
from math import floor
print("Q2", "floor(3.14159265359) retourne", floor(3.14159265359))

# Q3
def taille(entier):
    """
    Calcule la taille décimale d’un entier positif.
    CU : entier int ≥ 0
    Exemple :
    >>> taille(2014)
    4
    """
    return floor(log10(entier)) + 1

# Q4
print("Q4", "taille(2**100) retourne", taille(2**100))

# Q5
# Le code qui suit a été éxecuté dans l'interpréteur puis inseré ici en tant
# que commentaire pour garder le fichier valide car il provoque des erreurs







