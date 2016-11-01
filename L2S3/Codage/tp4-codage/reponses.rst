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

Question11.
tpcodings.py

Question12.

>>> decode_fixed_length_word('000100111000011000000011000100',coding1)
'CODAGE'

Question13.
On a obtenu: 'LA PHILANTHROPIE DE L OUVRIER CHARPENTIER'

>>> decode_fixed_length_word('01011000001111101111001110100001\
01100000011011001100111100010111\
00111101000001001111100011001001\
11110101111111011101010010101100\
01010000010010001111110001000111\
00000100010111100100011011001101\
0000010010001',coding1)
'LA PHILANTHROPIE DE L OUVRIER CHARPENTIER'

Le décodage pour les codages à virgule
======================================

Question14.
On teste la méthode find.

>>> x = 'this is first example'
>>> y = 'rst'
>>> x.find(y)
10
>>> z = 'on'
>>> x.find(z)
-1

Question15.
Fait tpcodings.py

Question16.
Resultat: 'POUR LA FRANCE D EN BAS DES NOUILLES ENCORE'

>>> decode_comma_word('.--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././', '/',coding2)
'POUR LA FRANCE D EN BAS DES NOUILLES ENCORE'

Le décodage pour les codages préfixes
=====================================

Question17.

>>> decode_prefix_letter('.--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././', coding2)
('P', 5)

On a obtenu un tuple ('P',5)

Question18.
J'ai un probleme avec cette exception :c
Question19.
J'ai obtenu: 'THALES EST TOUJOURS A FAIRE'

Stockage et lecture en binaire
==============================

Question20.
Le contenu d'un fichier file.txt c'est AB.
