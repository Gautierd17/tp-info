package jeu;
import jeu.util.*;

public class Joueur {
    private InputManager input;
    private Choix choix;
    private String name;

    /**
     * Initialization
     *
     * @param input input class used.
     * @param name Name of this player.
     */
    public Joueur(InputManager input, String name) {
        this.input = input;
        this.name = name;
    }

    /**
     * Pick option.
     */
    public void choisirOption() {
        String inp = input.getInput(name + " Option : Pierre, Feuille ou Ciseaux", "Pierre", "Feuille", "Ciseaux");

        switch (inp) {
            case "Pierre":
                choix = new Pierre();
                break;
            case "Feuille":
                choix = new Feuille();
                break;
            default:
                choix = new Ciseaux();
                break;
        }
    }

    /**
     * @return Returns the option picked or null.
     */
    public Choix getChoix() {
        return choix;
    }

    /**
     * @return Returns the name of the player.
     */
    public String getName() {
        return name;
    }
}
