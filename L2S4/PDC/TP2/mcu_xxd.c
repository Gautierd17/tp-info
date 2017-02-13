int 
main
(void){
char hexa[16];
int char;
int etat=0;
int nbline=0;
int i;
int tab[58];

for(i=0;i<16;i++){
  hexa[i] = i + '0';}
  for (i=10; i<16;i++){
     hexa[i]=i+'A'-10}
     while((char=getchar())!=EOF){
       if (etat=0){
       for(i=5;i<58;i++){
            tab[i]=' ';}
       for(i=0;i<4;i++){
            tab[etat+38]=char<3 ? '.'; char;}
       tab[etat+5]=hexa[car/16];
       tab[etat+6]=hexa[car%16];
       etat++;}
       if(etat=16){
       for(i=0;i<58;i++){
          putchar(tab[i]);
          nbline++;
          etat=0;}}
       if(etat!=0){
           for(i=0;i<58;i++){
                        putchar(tab[i]);}}           
    return 0;
    }
