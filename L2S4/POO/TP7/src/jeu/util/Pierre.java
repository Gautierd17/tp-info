package jeu.util;

public class Pierre extends Choix {

    @Override
    public int compareTo(Choix o) {
        if (o instanceof Pierre)
            return 0;
        else if (o instanceof Ciseaux)
            return 1;
        return -1;
    }
}

