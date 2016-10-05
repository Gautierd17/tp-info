from functions import *
# MAIN                                    
def main():
    """
    Application principale
    """
    # TITRE BEAUTIFUL
    header()
    # INITIALISER CHAMP DE MINES
    champ = init_champ()

    # GENERER AU HASAR ?
    HASARD = input("\nVoulez vous générer les bombes au hasard ? (oui/non)")
    grille = generer_bombes(HASARD[0].upper() == "O")
    
    # DEMANDER COORDONNÉES
    while True:

    	# AFFICHER CHAMP DE MINES
        print_champ(champ)

        # INPUT
        coordonnees = input_coordonnees()

        # BOMBE
        if(bombe(coordonnees, grille)):
            
            # AFFICHER CHAMP DE MINES
            champ[coordonnees[1]][coordonnees[0]] = "X"
            print_champ(champ)

            # BOOM
            print ("\n\n!!! BOOM !!!\n\n")

            # CONTNUER ?
            CONTINUE = input("\nVoulez vous rejouer ? (oui/non)")
            if(CONTINUE[0].upper() == "O"):
                champ = init_champ()

                # GENERER AU HASAR ?
                HASARD = input("\nVoulez vous générer les bombes au hasard ? (oui/non)")
                grille = generer_bombes(HASARD[0].upper() == "O")

                continue
            else:
                break
        else:
            # AFFICHER LA CASE
            afficher_case(champ, coordonnees[0], coordonnees[1], grille)

            # FIN DU JEU ?
            if(fin(champ, grille)):
                print ("\n\n!!! FÉLICITATIONS !!!\nVous avez localisé toutes les mines\n\n")

                # CONTNUER ?
                CONTINUE = input("\nVoulez vous rejouer ? (oui/non)")
                if(CONTINUE[0].upper() == "O"):
                    champ = init_champ()

                    # GENERER AU HASAR ?
                    HASARD = input("\nVoulez vous générer les bombes au hasard ? (oui/non)")
                    grille = generer_bombes(HASARD[0].upper() == "O")

                    continue
                else:
                    break


    
    # GAME OVER
    header("PARTIE TERMINÉE")

main()
