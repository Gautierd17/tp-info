#include "mcu_macro.h"
#include "mcu_readl.h"

int line[MAXLINE+1] ;

int
main
(void)
{
	int item, words;
	int words=0; 

	while((item=getchar()) != EOF){
		if((item == ' ') || (item=='\t')){ 
			 words++;
		}
		else{
			putchar(item);
		}
	}
	return 0;
}
