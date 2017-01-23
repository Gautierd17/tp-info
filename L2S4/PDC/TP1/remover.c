#include<stdio.h>

void startsby(int c);
void inside(void);
void quote(int c);

int main(void)
{
    int c;
    printf(" Print text with /* comment */ \n");

    while((c=getchar())!=EOF)
        startsby(c); 

    return 0;
}

void startsby(int c)
{
    int d;
    if( c == '/')
    {
        if((d=getchar())=='*')
         inside();
        else if( d == '/')
        {
            putchar(c);
            startsby(d);
        }
        else 
        {
            putchar(c);
            putchar(d);
        }
    }
    else if( c == '\''|| c == '"')
        quote(c);
    else
        putchar(c);
}

void inside()
{
    int c,d;
     
    c = getchar();
    d = getchar();

    while(c!='*' || d !='/')
    {
        c =d;
        d = getchar();
    }
}

void quote(int c)
{
    int d;

    putchar(c);
    
    while((d=getchar())!=c)
    {
        putchar(d);
        
        if(d = '\\')
            putchar(getchar());
    }
    putchar(d);
}
    