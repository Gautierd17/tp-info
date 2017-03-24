package jeu.util;
import java.util.Scanner;


public class InputManager {
    private Scanner scanner = new Scanner(System.in);

    /**
     * Receive input from the user.
     */
    public String getInput(String message, String... possibleInputs) {
        printLine(message);

        String input;
        while (true) {
            input = scanner.nextLine();

            if (isAllowedInput(input, possibleInputs))
                break;
            else
                printLine("Input is not correct\n" + message);
        }

        return input;
    }

    /**
     * Checks if 'input' is equal to "Pierre", "Feuille" or "Ciseaux".
     */
    private boolean isAllowedInput(String input, String[] possibleInputs) {
        for (int i=0; i<possibleInputs.length; i++)
            if (input.equals(possibleInputs[i]))
                return true;
        return false;
    }

    /**
     * Shows a message to the user.
     *
     * @param line The message to show.
     */
    public void printLine(String line) {
        System.out.println(line);
    }
}

