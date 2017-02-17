# TP 4 : Manipulations

### Etat:

**Exercice 1:**

 * Question 1 Fait
 * Question 2 Fait
 * Question 3 Fait
 * Question 4 Tests -- pas fait
 * Question 5 Fait
 * Question 6 Fait
 * Question 7 Fait

**Exercice 2:**

 * Fait

### Exercice 1.
**Q2 : Compilation**

La commande pour compiler des fichiers *.java* :

```shell
$ javac example/Robot.java -d ../classes
```
**Q3 : Documentation**

La commande pour générer javadoc:

```shell
javadoc example example.util -d ../docs
```

Modifications dans la documentation -- Box.java :

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

**Q4 : Tests**

Compilation du BoxTest.java :

```shell
javac -classpath test-1.7.jar test/BoxTest.java
```

Execution d'un test :

```shell
java -jar test-1.7.jar BoxTest
```

TestRobot.java a été fait mais j'ai obtenu des erreurs pendant la compilation.

**Q4 : Execution d'un programme**

Cette partie a été faite.

**Q5 : Archives**

##### Creation 

```
jar cvf ../appli.jar example
```

##### Utilisation

```
java -classpath appli.jar example.Robot
```
##### Extraction 

```
jar xvf appli.jar
```

##### JAR

```
jar cvfm ../appli.jar ../manifest-ex example
```

