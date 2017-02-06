
#include <stdio.h>
#include "mcu_macro.h"
#include "mcu_readl.h"
/*mcu_wc*/

int line[MAXLINE+1] ;
int
main
(void)
{
  int count=0;
  while(1){
  count+=readl(line);
  if (count==EOF) return count ; /* il faudra utiliser la fonction d'affichage vue en TD */
  }
  return 0;
}
