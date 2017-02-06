#include <stdio.h>
#include "mcu_macro.h"
int
readl
(int line[])
{
  int i =0 ;
  while(1){
    if (i==MAXLINE){
      /* appel a fatal a faire */
    }
    line[i] = getchar();
    if (line[i]==EOF) {
      line[i]='\0';
	return EOF ;
    }
    if (line[i]=='\n'){
      line[i]='\0';
      return i ;
    }

    i++ ;
  }
  return 0; 
}
