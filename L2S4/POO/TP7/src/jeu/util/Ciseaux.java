package jeu.util;

public class Ciseaux extends Choix {

    @Override
    public int compareTo(Choix o) {
        if (o instanceof Ciseaux)
            return 0;
        else if (o instanceof Feuille)
            return 1;
        return -1;
    }
}

