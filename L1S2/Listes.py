#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#Exercices sur les listes

import copy
from copy import deepcopy

#avec la fonction liste
def copie_liste0(old_list):
    new_list = list(old_list)
    return new_list
#avec l’opérateur de concaténation par ajouts successifs d’un élément de la liste à copier dans la liste copie ;
def copie_liste1(old_list):
    new_list = copy.copy(old_list)
    return new_list
#par création d’une liste en compréhension ;
def copie_liste2(old_list):
    new_list = old_list[ : ]
    return new_list
#par création d’une liste de même longueur que la liste à copier, puis report de ses éléments dans cette nouvelle liste.
#idk

month_lst = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 
              'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

nom_mois = int(input('Saissisez le numeéro du mois: '))
if nom_mois < 1 or nom_mois > 12:
    raise ValueError
else:
    print(month_lst[nom_mois - 1])    
    
def indice(index,liste):
    if index in liste:
        return index    
    else:
        print -1
        
def nbre_occurrences(index,liste):
    number_of_coincidences = liste.count(index)
    return number_of_coincidences 
