package jeu.util;

public class Feuille extends Choix {

    @Override
    public int compareTo(Choix o) {
        if (o instanceof Feuille)
            return 0;
        else if (o instanceof Pierre)
            return 1;
        return -1;
    }
}

