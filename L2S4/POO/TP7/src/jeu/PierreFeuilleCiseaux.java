package jeu;
import jeu.util.*;

/**
 * The class which allows us to create the game.
 *
 * @author iuliia shcherbakova
 *
 */
public class PierreFeuilleCiseaux {
    private InputManager input;
    private Joueur joueur1, joueur2;

    public PierreFeuilleCiseaux() {
        input = new InputManager();
    }

    /**
     * Detects the player who will start the game
     *
     * @param premierJoueur, True if joueur1 starts the game, False if joueur2.
     */
    public void commencerLeJeu(boolean premierJoueur) {
        input.printLine("On commence!");

        joueur1 = new Joueur(input, "Premier Joueur");
        joueur2 = new Joueur(input, "Deuxieme Joueur");

        if (!premierJoueur)
            swapPlayers();

        joueur1.choisirOption();
        joueur2.choisirOption();

        trouverGagnant();

        if (playAgain())
            commencerLeJeu(!premierJoueur);
    }

    /**
     * Gets who is the winner of the round
     */
    private void trouverGagnant() {
        int winner = joueur1.getChoix().compareTo(joueur2.getChoix());

        switch (winner) {
            case 1:
                input.printLine(joueur1.getName() + " Gagné!");
                break;
            case -1:
                input.printLine(joueur2.getName() + " Gagné!");
                break;
            case 0:
                input.printLine("Match Nul");
                break;
        }
    }

    /**
     * Will swap the two player references.
     */
    private void swapPlayers() {
        Joueur temp = joueur1;
        joueur1 = joueur2;
        joueur2 = temp;
    }

    /**
     * Play again
     *
     * @return True of False
     */
    private boolean playAgain() {
        String inp = input.getInput("Play again? - Oui/Non", "Oui", "Non");
        return inp.equals("Oui");
    }
}

