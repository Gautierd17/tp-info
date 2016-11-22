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
1.
2.
3.
4.
5.
6.

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
                                 
                                 
                                 
