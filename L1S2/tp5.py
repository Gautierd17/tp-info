# SHCHERBAKOVA Iuliia [GPE 45]
# TP5

#!/usr/bin/python
# -*- encoding: utf-8 -*-

display = __name__ == '__main__'
def partie(name):
    if display:
        print('\n***', 'Partie', name, '***')

partie("Programmation")

SEPARATEURS = "\n  \t     . ? ! , ; : - _ ' '' () [] {} + - * / = < >"

        
def decoupe_en_mots(chaine):
    assert type(chaine) == str
    return chaine.split(' ')

myfile = open('cigale.txt')  
lines = myfile.readlines()  
list_of_elements = []
for line in lines:
    nline=''
    for i in range(len(line)):
        if line[i] in SEPARATEURS:
            nline+=' '
        else:
            nline+=line[i]
    list_of_elements += nline.split()
myfile.close()

# >>> len(list_of_elements)
# 114

partie("Analyser un fichier texte")

def analyse(canal):
    """
Cette fonction est paramétrée par un canal supposé ouvert en lecture sur\
un fichier texte, et qui renvoie un triplet (l,m,c).

CU: aucune

>>> analyse('cigale.txt')
(24, 114, 494)

    """
    assert (type(canal) == str)
    myfile = open(canal)
    l = sum(1 for line in myfile)
    m = len(list_of_elements)
    string = ''.join(list_of_elements)
    c = len(string)
    return l,m,c

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)

# SHCHCHERBAKOVA Iuliia [GPE 45]
# TP5

display = __name__ == '__main__'
def partie(name):
    if display:
        print('\n***', 'Partie', name, '***')


partie("le thème du TP")

print("-l : afficher le nombre de lignes")
print("24 cigale.txt")
print("-w : afficher le nombre de mots")
print("108 cigale.txt")
print("-c : afficher le nombre d’octets")
print("639 cigale.txt")
print("-lw : afficher le nombre de lignes et de mots")
print("24 108 cigale.txt")
print("-lc : afficher le nombre de lignes et d’octets")
print("24 639 cigale.txt")
print("-wc : afficher le nombre de mots et d’octets")
print("108 639 cigale.txt")
print("-lwc : afficher le nombre de lignes, de mots et d’octets")
print("24 108 639 cigale.txt")
print("Pour le vide.txt 0, 00, ou 000 partout")

partie("Les arguments sur la ligne de commandes")

print("Pour chaque invocation de Python, sys.argv est automatiquement\
une liste de chaînes représentant les arguments\
(séparés par des espaces) dans le terminal.\
Le nom vient de la convention de programmation C dans laquelle argv et argc\
représentent les arguments du terminal(command-line).")
