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
  strrev(count);
  if (count==EOF) putchar(count) ; 
  }
  return 0;
}

#include <stdio.h>

#define Num   MAXLINE

int main( void ) 
{
    char str[Num], revstring[Num];

    
    getchar(str, Num, stdin);

    size_t  length = 0;
    while (str[length] != '\0' && str[length] != '\n') ++length;

    if (str[length] == '\n') str[length] = '\0';

    size_t i = 0;
    for (i != length; i++) revstring[i] = str[length - i - 1];

    revstring[i] = '\0';

    putchar(revstring);

    return 0;
}
