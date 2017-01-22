#include <stdio.h>

#define VAL 2
/* ceci est un commentaire */

/* ceci est un commentaire 
   sur plusieurs ligne     */

int je_ne_suis_pas_defini;

int variable_de_classe_externe;



int
main
(void)
{
  int variable_automatique = 3;
  variable_de_classe_externe = VAL;
  variable_automatique += je_ne_suis_pas_defini;
  
  return variable_automatique-variable_de_classe_externe;
}
