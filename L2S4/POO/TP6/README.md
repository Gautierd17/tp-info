SHCHERBAKOVA Iuliia
L2S4 Info G4
10/03

[![UNIX](https://img.shields.io/badge/unix-commands-009999.svg)](https://www.tjhsst.edu/~dhyatt/superap/unixcmd.html)
[![GITLAB](https://img.shields.io/badge/gitlab-documentation-33CCCC.svg)](https://docs.gitlab.com)
[![JAVA](https://img.shields.io/badge/java-documentation-00FFCC.svg)](https://docs.oracle.com/javase/8/)
[![TP6 SUJET](https://img.shields.io/badge/tp6-manipulation%20d'images-99FFCC.svg)](http://www.fil.univ-lille1.fr/%7Eroutier/enseignement/licence/poo/tdtp/image.pdf)


# TP 6 : Manipulation d'images

Le but du TP6 consiste à mettre en place des manipulations suivantes: creation des paquetages, compilation des fichiers `.java`, génération de la documentation, creation des tests, creation des archives et execution du programme.

## Etat :

  * **Q1 :**
  * **Q2 :**
  * **Q3 :**
  * **Q4 :**
  * **Q5 :**
  * **Q6 :** *Fait*

## Q1. Les couleurs

| image::color::GrayColor  | Priv/Pub | 
| ------------- | -------| 
| **WHITE  : GrayColor**  | + | 
| **BLACK : GrayColor**  | + | 
| **int : grayLevel**  | - | 
| GrayColor(level : int)  | + | 
| getGrayLevel : int  | + | 
| equals(o : Object) : boolean  | + | 

## Q2. Les Pixels
Pour compiler des paquetages créés dans la question precedente on utilise la commande suivante depuis le dossier **src**.

```
$ javac example/Robot.java -d ../classes
```
*-d : une option qui permet de préciser le dossier destination de la compilation*

## Q3. Les Images
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

## Q4. Class ImageExample
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

## Q5. Exécution du programme : ImageMain

Résultat d'exécution du programme depuis le terminal:

```
$ java example.Robot
beginning of main from robot.Robot
the conveyer belt carries2 box(es)
a box of weight 10
a box of weight 15
end of main from robot.Robot
```

## Q6. Rendu TP6

La commande **jar** nous permet de créer/consulter/extraire des archives.

Voici la liste des commandes:

* Création : `$ jar cvf ../appli.jar example`
* Consultation : `$ jar tvf appli.jar`
* Utilisation : `$ java -classpath appli.jar example.Robot`
* Extraction : `$ jar xvf appli.jar`
* JAR : `$ jar cvfm ../appli.jar ../manifest-ex example` --> `$ java -jar appli.jar`
*(il faut ajouter le fichier manifest-ex dans le dossier TP4)*
