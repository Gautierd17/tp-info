#include "mcu_macro.h"
#include "mcu_readl.h"

int line[MAXLINE+1] ;

int
main
(void)
{
  int count =0 ;

 readl(line);
  return 0;
}
