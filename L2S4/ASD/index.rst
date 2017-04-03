-----------------
tp-arbresbinaires
-----------------

~~~~~~~~~~
Etat du TP
~~~~~~~~~~

Partie 5.2 :
  * 5.2.1 : Fait
  * 5.2.2 : Fait
  * 5.2.3 : Fait
Partie 5.3 :
  * Q1 : Fait
  * Q2 : Fait
  * Q3 : Fait
  * Q4 : Fait
  * Q5 : Fait
  * Q6 : Pas Fait
  * Q7 : Fait
Partie 5.4 :
  * Q1 : Fait
  * Q2 : Pas Fait

~~~~~~~~~~~~
Fichiers TP
~~~~~~~~~~~~
  * exemple1_arbre.c :: arbre binaire 1
  * exemple2_arbre.c :: arbre binaire 3
  * exemple3_arbre.c :: arbre binaire 2
  * abr1_arbre.c :: ABR 1
  * abr2_arbre.c :: ABR 2
  * abr3_arbre.c :: ABR 3
  * Test_arbre.c :: fonctions et tests
  * Affichage.c :: programme d'Affichage
  * ArbreBinaire.c :: module arbre binaire

Les arbres.pdf se trouvent dans le dossier images.
~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

Question 5.2.3.(5)
------------------
Des valeurs de factoriels plus grandes que 20! sont negatifs parce que la
limite de unsigned long est en fait 2147483647.

Question 5.3.(2)
----------------
Par définition, Un arbre binaire a est un arbre binaire de recherche si,
pour tout nœud s de a, les contenus des nœuds du sous-arbre gauche de s
sont strictement inférieurs au contenu de s, et que les contenus des
nœuds du sous-arbre droit de s sont strictement supérieurs au contenu
de s.
Par example, on a AB:
          a
        /   \
       b     c
     /  \
    d    e

Pour vérif si AB est ABR on doit prouver que:
  1) a>b
  2) a<c
  3) b>d
  4) d<e

Implementation C
----------------
.. code-block:: c
   :emphasize-lines: 3,5

       int isABR(Noeud_t abr)
    {
      if (abr == NULL)
        return(true);

      if (abr->filsgauche!=NULL && valeur_maximale(abr->filsgauche) > abr->val)
        return(false);

      if (abr->filsdroit!=NULL && valeur_minimale(abr->filsdroit) < abr->val)
        return(false);

      if (!isABR(abr->filsgauche) || !isABR(abr->filsdroit))
        return(false);
      return(true);
    }

.. toctree::
   :maxdepth: 1
