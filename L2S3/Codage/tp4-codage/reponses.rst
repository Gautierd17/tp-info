TP4-Codages et décodages

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
Fait sur fichier python functions.py

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







