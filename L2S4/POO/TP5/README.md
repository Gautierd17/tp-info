# TP 5 : Tours de Hanoi

[![UNIX](https://img.shields.io/badge/unix-commands-d600ff.svg)](https://www.tjhsst.edu/~dhyatt/superap/unixcmd.html)
[![GITLAB](https://img.shields.io/badge/gitlab-documentation-6500ff.svg)](https://docs.gitlab.com)
[![JAVA](https://img.shields.io/badge/java-documentation-0085ff.svg)](https://docs.oracle.com/javase/8/)
[![TP5 SUJET](https://img.shields.io/badge/tp5-tours%20de%20hanoi-00f6ff.svg)](http://www.fil.univ-lille1.fr/%7Eroutier/enseignement/licence/poo/tdtp/tp-hanoi.pdf)

Le but de TP5 consiste à mettre en place des manipulations suivantes: creation des classes : `Hanoi.java`, `Tower.java` et `Dics.java`, compilation de classes `.java`, génération de la documentation, creation des tests pour des classes créés, creation des archives et execution du programme(affichage basique/plus visuel).

## Etat :

  * **Q1 :** *Fait*
  * **Q2 :** *Fait*
  * **Q3 :** *Pas Fait*
  * **Q4 :** *Fait version basique*

## Q1. La résolution complète du problème de Hanoi
Pour resoudre le probleme de Hanoi on doit créér des paquetages suivants `hanoi.Hanoi`, `hanoi.util.Tower` et `hanoi.util.Disc`. On fait des tests pour verifier si le code fonctionne bien.

Pour executer le test :

```
$ java -jar test-1.7.jar TestHanoi
```

Comme noté dans le TP precedent :
> Les paquetages servent à structurer l'ensemble des classes et interfaces écrits en Java. Les noms de paquetage prennent une forme telle que `mainJava.monPaquet`. Si la classe `newClass` se trouve dans un paquetage `mainJava.monPaquet`, alors son nom complet est `mainJava.monPaquet.newClass`. Le fichier `newClass.class` sera nécessairement rangé dans un répertoire de nom **monPaquet** contenu par un répertoire de nom **mainJava**. Autrement dit, la fin du chemin d'accès à ce fichier sera **mainJava/monPaquet**.

## Q2. Hanoi.Main
On fait la version basique qui résout le problème des tours de Hanoi pour un nombre de disques donnée. Pour executer le progamme on utlise la commande suivannte (../classes) :

```
$ java hanoi.HanoiMain
```

## Q3. Version interactive.

Pas reussi à faire.

## Q4. JAR

### Pour info
### Gestion d'archives

La commande **jar** nous permet de créer/consulter/extraire des archives.

Voici la liste des commandes:

* Création : `$ jar cvf ../appli.jar example`
* Consultation : `$ jar tvf appli.jar`
* Utilisation : `$ java -classpath appli.jar example.Robot`
* Extraction : `$ jar xvf appli.jar`
* JAR : `$ jar cvfm ../appli.jar ../manifest-ex example` --> `$ java -jar appli.jar`
*(il faut ajouter le fichier manifest-ex dans le dossier TP4)*

### Ajouter des ressources

> Il est possible d’ajouter des ressources autres que les dossiers des classes `a une archive jar. Par exemple on peut vouloir ajouter le dossier docs contenant la documentation. Pour conserver le niveau de dossier docs dans l’archive, il faut avant de l’inclure se “placer au-dessus” de ce dossier et donc **C**hanger de dossier par l’option **-C**

```
$ jar cvfm ../appli.jar ../manifest-ex example -C .. docs -C .. test
$ jar cvfm appli.jar manifest-ex docs test -C classes example
```
