#include "mcu_macro.h"
#include "mcu_readl.h"

int line[MAXLINE+1] ;

int
main
(void)
{
	int item, lines;
	int lines=0; 

	while((item=getchar()) != EOF){
		if(item == "\n"){
			 lines++;
		}
		else{
			putchar(item);
		}
	}
	return 0;
}
