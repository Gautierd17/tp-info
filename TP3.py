#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#TP 3 http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_conditionnelle.html
#Autour du calendrier

#Années bissextiles

def est_divisible_par(a,b):
    if a%b == 0:
        return True
    else:
        return False


def est_bissextile(year):
   if((year % 4) == 0):
      if((year % 100) == 0):
         if( (year % 400) == 0):
            return 1
         else:
            return 0
      else:
         return 1
   return 0
 
n = 0
print "Program to check Leap Year"
print "Enter Year: ", 
n = input()
if( IsLeapYear(n) == 1):
   print n, "is a leap year"
else:
   print n, "is NOT a leap year"
   
#Nombre de jours dans un mois

import datetime
import calendar
 
nbre_jours = ( ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ), ( 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )
 
leapYear = calendar.isleap(datetime.datetime.now().year)
 
while True:
    try:
        monthNumber = int(input('Month number (1 - 12): '))
        print("%d day%s" % (nbre_jours[leapYear][nbre_jours - 1], '' if nbre_jours[leapYear][nbre_jours - 1] & 1 else 's'))
    except:
        print('Bye')
        break

#Nombre de jours 2

import datetime
import calendar

nbre_jours = ( ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ), ( 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )

def nbre_jours(m,a):
    if m > 12 and m < 1:
        print('ValueError')
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print('31')
    if m == 4 or m == 6 or m == 9 or m == 11:
        print('30')
    if m == 2 and a % 4 or 100 or 400 == 0:
        print(' REMARQUE: si l annÃ©e est bissextile nbre_jours(m == 2) = 29')
    if m == 2:
        print('si l annÃ©e n est as bissextile nbre_jours(m = 2) = 28')
    
    
    return nbre_jours

#Condition dâ€™utilisation et instruction assert
#README QUESTIONS

#Date valide

def est_date_valide(j,m,a):
    while j < 32 and j > 0 and m < 13 and m > 0 and a > -1:
        return True
    else:
        return False
        
#Date valide

def est_date_valide(j, m, a):
    """
    Indique si la date donnée appartient au calendrier grégorien.
    CU : -aucune-
    Exemple :
    >>> est_date_valide(25, 4, 1983)
    True
    """
    return type(j) is int and type(m) is int and type(a) is int and a > 1582 \
        and m in range(1, 13) and j in range(1, nbre_jours(m, a)+1)

#Numéro du jour dans la semaine

def corrige_mois(m, a):
    """
    Renvoie la valeur corrigée du mois selon l’algorithme de Delambre.
    CU : m entier, a entier, 1 ≤ m ≤ 12, a > 1582
    Exemple :
    >>> corrige_mois(2, 2016)
    6
    """
    assert(type(a) is int and a > 1582), \
        "L'année doit être un entier supérieur à 1582"
    assert(type(m) is int and m in range(1, 13)), \
        "Le mois doit être un entier compris entre 1 et 12 inclus"

    liste_corrections_mois = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
   
    if est_bissextile(a):
        liste_corrections_mois[0] = 3
        liste_corrections_mois[1] = 6

    return liste_corrections_mois[m-1]
    
def num_jour(j, m, a):
    """
    Renvoie le numéro du jour dans la semaine correspondant à la date donnée.
    CU : Date valide (selon est_date_valide())
    Exemple :
    >>> num_jour(9, 11, 2004)
    2
    """
   
    assert(est_date_valide(j, m, a)), "La date n'est pas valide"
 
    ab = a//100
    cd = a%100
    return (cd//4 + ab//4 + cd + corrige_mois(m, a) + j + 2 + 5 * ab) % 7

# [Tests]
# >>> num_jour(9, 11, 2004)
# 2
# >>> num_jour(24, 10, 1929)
# 4


def nom_jour(j, m, a):
    """
    Renvoie le nom du jour dans la semaine correspondant à la date donnée.
    CU : Date valide (selon est_date_valide())
    Exemple :
    >>> nom_jour(24, 10, 1929)
    "Jeudi"
    """
    assert(est_date_valide(j, m, a)), "La date n'est pas valide"
    num = num_jour(j, m, a)
   
    assert(num in range(7)), "Jour de la semaine inconnu"
    
    liste_jours_semaine = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", \
        "Vendredi", "Samedi"]
    return liste_jours_semaine[num]
    
    #Imprimer le calendrier d’un mois
    
def imprimer_mois(m, a):
    """
    Imprime le calendrier du mois de l'année donné.
    CU : m entier, a entier, 1 ≤ m ≤ 12, a > 1582
    Exemple :
    >>> imprimer_mois(9, 2014)
       Septembre 2014
    di lu ma me je ve sa
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30
    """
    assert(type(a) is int and a > 1582), \
        "L'année doit être un entier supérieur à 1582"
    assert(type(m) is int and m in range(1, 13)), \
        "Le mois doit être un entier compris entre 1 et 12 inclus"

    # Affichage mois et année
    # On stocke les mois dans un tableau pour un accès facilité
    liste_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", \
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    # On enlève 1 à l'index du tableau, car les mois comment à 1
    # alors que le tableau commence lui à 0
    # On stocke dans une variable le titre brut (sans alignement / espacement)
    titre = liste_mois[m-1] + " " + str(a)
    # On affiche le titre centré en répètant sur la droite un certain nombre
    # de caractères d'espacements. Ce dernier est calculé en enlevant la
    # longueur du titre àl a longueur maximale de la ligne et en divisant le
    # tout par deux
    print(" " * ((20-len(titre))//2) + titre)
    # Affichage nom des jours de la semaine
    print("di lu ma me je ve sa")
    # Affichage des jours
    jour = 1 # Le jour à écrire (s'incrémente)
    jour_semaine_1er = num_jour(jour, m, a) # Premier jour de la semaine
    nbre_jours_mois = nbre_jours(m, a) # Nombre de jours du mois
    # Boucle sur les lignes.
    # Ne s'arrête pas tant que le jour final a été atteint
    while jour <= nbre_jours_mois:
        # La variable ligne stockera la ligne avant de l'imprimer
        ligne = "" # On l'initialise / l'efface
        # Boucle sur les jours de la semaine.
        for jour_semaine in range(7):
            # Si on en est au premier jour (donc sur la première ligne) mais que
            # le premier jour n'a pas été dépassé, on ajoute du "vide"
            if jour == 1 and jour_semaine < jour_semaine_1er:
                ligne += "  "
            # Sinon, et si on a pas dépassé le nombre de jours
            elif jour <= nbre_jours_mois:
                # On ajoute un caractère d'espacement si le nombre ne possède
                # qu'un chiffre pour l'aligner à droite
                if jour < 10:
                    ligne += " "
                # On ajoute le nombre du jour
                ligne += str(jour)
                # On incrémente jour pour passer au prochain jour
                jour += 1
            # Si on est entre deux jours, on ajoute un caractère d'espacement
            if jour_semaine < 6 and jour <= nbre_jours_mois:
                ligne += " "
        print(ligne) # On affiche la ligne
    
    
    
