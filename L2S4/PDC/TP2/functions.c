#include <string.h>

void reverse(char s[])
{
    int length = strlen(s) ;
    int c, i, j;

    for (i = 0, j = length - 1; i < j; i++, j--)
    {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

int main()
{
    fstream myfile;
    myfile.open("test.txt",ios::in);
    
    fstream outfile;
    outfile.open("output.txt",ios::out|ios::app);
    map<string,int> mymap;
    string cur;
    while(getline(myfile,cur)){
        if(mymap[cur]==NULL){
            mymap[cur]=1;
            outfile.write(cur.c_str(),cur.length());
            outfile.put('\n');
        }
        else
            mymap[cur]++;
    }
    outfile.close();
    myfile.close();
}
