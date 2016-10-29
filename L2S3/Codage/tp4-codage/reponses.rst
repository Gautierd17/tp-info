TP4-Codages et décodages
########################

Le module Coding
================

:: 1.3 Premier essai du module ::
*********************************

Pour des trois questions suiv. on defin. des consts:

>>> source_alphabet = ['a', 'b', 'c']
>>> code=['010','100','110']
>>> my_coding=create(source_alphabet,code)

Question2.

>>> my_coding.code('a')
'010'
>>> my_coding.code('b')
'100'
>>> my_coding.code('c')
'110'

Question3.

>>> my_coding.decode('010')
'a'
>>> my_coding.decode('100')
'b'
>>> my_coding.decode('110')
'c'


Question4.
On obtient une erreur 'Not_codable_symbol'.

Question5.
On obt. une erreur 'Undecodable_word'.

Les codages utilisés dans le TP
===============================

:: 2.3 Création des codages ::
******************************

Question6.
Fait sur fichier python tpcodings.py

Question7.
On a testé trois variables: coding1,coding2 et coding3, pour un lettre 'S'.

>>> coding1.code('S')
'10010'
>>> coding2.code('S')
'.../'
>>> coding3.code('S')
'1011'

La fonction de codage
=====================
Question8.
Fait dans le fichier tpcodings.py

Question9.
On verif si notre fonctionne donne le bon résultat.

>>> code_word('CODAGE',coding1) == '000100111000011000000011000100'
True
>>> code_word('CODAGE',coding2) == '-.-./---/-../.-/--././'
True
>>> code_word('CODAGE',coding3) == '0100100000111010100111110110'
True

Donc, ça marche bien.

Le décodage pour les codages de longueur fixe
=============================================
Question10.
On sait que la longueur que chaque element du coding1 possede la longueur egale à 5. Donc chaque lettre est codé par 5 chiffres.

Pour verifier cette conclusion j'ai fait un predicat check() qui renvoie True si la longueur de chaque element est egale à 5.

def check():
    for i in code1:
        if len(i)==5:
            return True
        return False


>>> check()
True

Donc, l'expression qui permet de connaître la longueur commune des mots:

>>> len(codeword)%5 != 0





