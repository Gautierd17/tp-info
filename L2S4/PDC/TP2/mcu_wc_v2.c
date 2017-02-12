#include <stdio.h>
#include "mcu_macro.h"
#include "mcu_readl.h"
/*mcu_wc*/

int line[MAXLINE+1] ;
int
main
(void)
{
  int char=0;
  int count=0;
  while ((char = getchar ()) !=EOF){
  char++;
  count+=readl(line);
  if (count==EOF){
  putchar(char) ;} 
  }
  return 0;
}
