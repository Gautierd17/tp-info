# TP 4 : Manipulations

[![UNIX](https://img.shields.io/badge/unix-commands-d600ff.svg)](https://www.tjhsst.edu/~dhyatt/superap/unixcmd.html)
[![GITLAB](https://img.shields.io/badge/gitlab-documentation-6500ff.svg)](https://docs.gitlab.com)
[![JAVA](https://img.shields.io/badge/java-documentation-0085ff.svg)](https://docs.oracle.com/javase/8/)
[![TP4 SUJET](https://img.shields.io/badge/tp4-manipulations-00e5ff.svg)](http://www.fil.univ-lille1.fr/%7Eroutier/enseignement/licence/poo/tdtp/tp4.pdf)

Le but de TP4 consiste à mettre en place des manipulations suivantes: creation des paquetages, compilation des fichiers `.java`, génération de la documentation, creation des tests, creation des archives et execution du programme.

## Etat :

  * **Q1 :** *Fait* 
  * **Q2 :** *Fait*
  * **Q3 :** *Fait*
  * **Q4 :** *Fait*
  * **Q5 :** *Fait*
  * **Q6 :** *Fait*
  * **Q7 :** *Fait*
  
## Q1. Mise en œuvre des paquetages
Les paquetages servent à structurer l'ensemble des classes et interfaces écrits en Java. Les noms de paquetage prennent une forme telle que `mainJava.monPaquet`. Si la classe `newClass` se trouve dans un paquetage `mainJava.monPaquet`, alors son nom complet est `mainJava.monPaquet.newClass`. Le fichier `newClass.class` sera nécessairement rangé dans un répertoire de nom **monPaquet** contenu par un répertoire de nom **mainJava**. Autrement dit, la fin du chemin d'accès à ce fichier sera **mainJava/monPaquet**.

## Q2. Compilation
Pour compiler des paquetages créés dans la question precedente on utilise la commande suivante depuis le dossier **src**.

```
$ javac example/Robot.java -d ../classes
```
*-d : une option qui permet de préciser le dossier destination de la compilation*

## Q3. Génération de la documentation
Tout d'abord, il faut completer la documentation de la classe `Box.java`.

```java
// les methodes de la classe Caisse 
    /** 
     * returns a weight of created Box
     * @return weight of the created Box
     */
    public int getWeight() {
        return this.weight;
    }
```

Après on utilise la commande suivante pout créer **javadoc**.

```
$ javadoc -d ../docs -subpackages example
// OU
$ javadoc example example.util -d ../docs
```

## Q4. Tests
Pour tester la classe `Robot.java` j'ai créé un test `TestRobot.java`. Voici le code:

```java
import org.junit.*;
import static org.junit.Assert.*;

import example.Robot;
import example.util.Box;
import example.util.ConveyerBelt;

public class TestRobot {

    @Test
    public void testTake() {
        Robot newRobot = new Robot();
        Box newBox1 = new Box(10);
        newRobot.take(newBox1); // box has been taken
        assertNotNull(newRobot.carryBox());
    }

    @Test
    public void testCarryBox() {
        // case 1 : box has been taken
        Box someBox1 = new Box(10);
        Robot someRobot1 = new Robot();
        someRobot1.take(someBox1);
        assertTrue(someRobot1.carryBox());

        // case 2 : no box taken
        Box someBox2 = new Box(20);
        Robot someRobot2 = new Robot();
        ConveyerBelt belt = new ConveyerBelt(100);
        someRobot2.take(someBox2);
        someRobot2.putOn(belt);
        assertFalse(someRobot2.carryBox());
      }

    @Test
    public void testPutOn() {
        Robot createRobot = new Robot();
        Box createBox = new Box(10);
        ConveyerBelt createBelt = new ConveyerBelt(100);
        createRobot.take(createBox); // take a box
        createRobot.putOn(createBelt); // put box on belt
        // belt is not full now (capacity = 2)
        assertFalse(createBelt.isFull());
        assertFalse(createRobot.carryBox()); // robot don't have any box now

        // testing if belt is full
        Box createBox2 = new Box(20);
        createRobot.take(createBox2);
        createRobot.putOn(createBelt);
        assertTrue(createBelt.isFull());
      }


    // ---Pour permettre l'exécution des test----------------------
    public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(TestRobot.class);
    }

}

```

Pour compiler ce test on utilise la commande suivante depuis la racine du projet:

```
$ javac -classpath test-1.7.jar test/TestRobot.java
```

Maintenant on peut exécuter le test:

```
$ java -jar test-1.7.jar TestRobot
```

## Q5. Exécution du programme

Résultat d'exécution du programme depuis le terminal:

```
$ java example.Robot
beginning of main from robot.Robot
the conveyer belt carries2 box(es)
a box of weight 10
a box of weight 15
end of main from robot.Robot
```

## Q6. Gestion d'archives

La commande **jar** nous permet de créer/consulter/extraire des archives.

Voici la liste des commandes:

* Création : `$ jar cvf ../appli.jar example`
* Consultation : `$ jar tvf appli.jar`
* Utilisation : `$ java -classpath appli.jar example.Robot`
* Extraction : `$ jar xvf appli.jar`
* JAR : `$ jar cvfm ../appli.jar ../manifest-ex example` --> `$ java -jar appli.jar`
*(il faut ajouter le fichier manifest-ex dans le dossier TP4)*

## Q7. Ajouter des ressources

> Il est possible d’ajouter des ressources autres que les dossiers des classes `a une archive jar. Par exemple on peut vouloir ajouter le dossier docs contenant la documentation. Pour conserver le niveau de dossier docs dans l’archive, il faut avant de l’inclure se “placer au-dessus” de ce dossier et donc **C**hanger de dossier par l’option **-C**

```
$ jar cvfm ../appli.jar ../manifest-ex example -C .. docs -C .. test
$ jar cvfm appli.jar manifest-ex docs test -C classes example
```
