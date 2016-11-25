Entropie par octet
==================

Q1.
Quelle est la valeur maximale de l’entropie d’un fichier ?

Pour toute source on a 0<=H(S)<=log(2)m, où H(S) est l'entropie d'une source S.
L'entropie d'une source est maximale , c.a.d., égale à log(2)m si et seulement si la distribution de probabilité est uniforme.

Pour quels fichiers est-elle atteinte ?
Dans notre cas la probabilité d’un symbole (octet) s est représentée par la formule: Pr(S=s) = n(s)/N
	-n(s) : le nombre d’occurrences de s dans le fichier 
	-N : la taille (en nombre d’octets) du fichier

Comme la taille du fichier reste constante, on peut dire que l'entropie est maximale si et seulement si la valeur du n(s)  la valeur est la même pour chaque symbole.
On peut faire la conclusion plus générale. L'entropie maximale apparaît lorsque les octets sont distribués de façon égales à travers le fichier, et qu'il n'est plus possible le compresser d'avantage.
Q2. 
Par la formule générale:
	H(S) = (m)somme[i=1] Pr(S=s)*I(s)= -(m)somme[i=1] p(i) log(2){p(i)}

Dans notre cas:
	* Pr(S=s(i))=p(i)=n(s)/N
	* i=s=0
	* m=255
	* I(s)=log(2){p(i)}

Donc la formule devient:
	H(s) = -(255)somme[s=0] n(s)/N * log(2){n(s)/N}
	= -(255)somme[s=0] n(s)/N * (log(2)n(s) - log(2)N)
	= -(255)somme[s=0] [n(s) * (log(2)n(s) - log(2)N)]/N
	= log(2)N - (255)somme[s=0] [n(s) * (log(2)n(s))]/N

Q3.
Fait (entropy.py)

Q4.
Résultats:
1. cigale.txt | 3.7991953737198085 bits per byte
2. sonnet18.txt | 3.9739164935644125 bits per byte
3. entropy_skeleton.py | 4.472445544178845 bits per byte
4. codage.bmp | 7.669807324168044 bits per byte, codage.png | 6.570247196020586 bits per byte
5. tp3-codage.zip | 6.017314629059505 bits per byte
6. morse.mp3 | 6.902062818381617 bits per byte, morse.wav | 7.71437728328608 bits per byte

Estimation de la taille d’un fichier optimalement codé
======================================================

Q5.
Pour répondre à cet question nous utilisons un théorème du codage sans bruit donc, autrement dit nous allons réduire la quantité de données (la longueur de la séquence) en faisant la moyenne des probabilités d'éléments dans la séquence codée.
On sait que par théorème du codage sans bruit, la longueur moyenne n des mots de tout code déchiffrable est
bornée inférieurement selon:
	H(S)/log(2)q <= n(c) , où q>=2
Donc la conséquence de cet théorème est que, si la longueur moyenne d'un codage atteint la valeur minimale donnée par ce théorème, c.a.d:
	H(S)/log(2)q = n(c) , où q>=2
le codage est optimal. 
On peut aussi dire que notre codage est optimal si la probabilité de chaque symbole est la même.
Selon N = m^n, pour transmettre N non récurrent messages utilisant m symboles d'un alphabet, les symboles devraient être combinés en n morceaux dans le mot de code.
Pour ce codage optimal, si le source contient N symboles, l'entropie est H(S)=log(2)N. Donc la longueur des mots de code est égale à n = logN/log(m) 

Q6. 
Fait (entropy.py)

Shannon-Fano algo:
                    ABCDE
              ....>       <...
            AB                CDE
        <...   ...>       <...   ...>
      A            B     C           DE
                                 <...  ....>
                                 D          E
                                 
                                 
Dans le codage de Shannon-Fano, les symboles sont disposés dans l'ordre du plus probable au moins probable, puis divisés en deux ensembles dont les probabilités totales sont aussi proches que possible de l'égalité.

Q7. 
Résultats:
1. cigale.txt | 41.872815172828915%
2. sonnet18.txt | 51.95812869587762%
3. entropy_skeleton.py | 36.527512018599474%
4. codage.bmp | 26.906682486648858%, codage.png | 19.010586543255727%
5. tp3-codage.zip | 21.37481862265539%
6. morse.mp3 | 18.8635193319918%, morse.wav | 21.8747403456158%

Mise en œuvre de l’algorithme de Huffman
========================================

Q8.
Fait (huffman_skeleton.py)

Q9.
On utilise symbol_list pour créer une liste des elements d'une dict passée en paramentre.
On utilise tree_list comme le stack pour ajouter ou supprimer des elements.

Q10, Q11.
Le programme fonctionne bien, mais pas bien fait.

Q12. 
Exemple d'utilisation du codage de Huffman:
On a un fichier de 100 ocetet dans lequel tous les mots sont écrits utilisant 6 symboles differents. Par exemple:
A,B,C,D,E,F.
On a calculé le nombre des probabilités de chaque symbole dans le fichier:
A : 10 
B : 20
C : 30
D : 5
E : 25
F : 10

On réunit les deux arbres de probabilité les plus petites en un unique arbre, sa probabilité
étant égale à la somme des deux probabilités des arbres réunis.

30    10     5     10     20     25
 C     A     D      F      B      E
             |     |
             |--|--|
               ||-|
               |15|  = 5 + 10
               |--|
(étape 1)
On procède ensuite de la même façon jusqu'à obtenir une forêt ne contenant plus qu'un seul
arbre.

30    10     5     10     20     25
 C     A     D      F      B      E
       |     |      |
       |     |      |
       | |--||      |
       |-|15||      |
         ||-|       |
          |         |
          |    |--| |
          |----|25|-| = 10 + 15
	       |--|

(étape 2)

30    10     5     10     20     25
 C     A     D      F      B      E
 |     |     |      |      |      |
 |     |     |      |      |      |
 |     | |--||      |      |      |
 |     |-|15||      |      |      |
 |       ||-|       |      |      |
 |        |         |      |      |
 |        |    |--| |      | |--| |
 |        |----|25|-|      |-|45|-|
 |             ||-|          ||-|
 |    |--|      |             |
 |----|55|------|             |
      |-||                    |
        |   |------------|    |
        |---| Root (100) |----|
            |------------|

(étape n)

Maintenant on peut définir le codage optimal.
   C = 00   (2 bits)
   A = 0100 (4 bits)
   D = 0101 (4 bits)
   F = 011  (3 bits)
   B = 10   (2 bits)
   E = 11   (2 bits)
   
       |----------|----------------|-------------------|--------------|
       |   Freq.  |    Au début    |   Après Hauffman  |  Différence  |
       |----------|----------------|-------------------|--------------|
       |  C 30    |  30 x 8 = 240  |    30 x 2 = 60    |      180     |
       |  A 10    |  10 x 8 =  80  |    10 x 3 = 30    |       50     |
       |  D 5     |   5 x 8 =  40  |     5 x 4 = 20    |       20     |
       |  F 10    |  10 x 8 =  80  |    10 x 4 = 40    |       40     |
       |  B 20    |  20 x 8 = 160  |    20 x 2 = 40    |      120     |
       |  E 25    |  25 x 8 = 200  |    25 x 2 = 50    |      150     |
       |----------|----------------|-------------------|--------------|   
       Taille initiale d'un fichier : 100octet=800bits
       Après compression: 30octet=240bits
       

