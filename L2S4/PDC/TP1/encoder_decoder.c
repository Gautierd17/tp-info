#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 

void decrypt(char arr[])
{
	int i;
	for(i = 0; i < strlen(arr); i++)
	{
		if (arr[i] == 'a')
			 arr[i] = 'l';
	}
}
 
void encrypt(char arr[])
{
	int i;
	for(i = 0; i < strlen(arr); i++)
	{
		if (arr[i] == 'l')
			arr[i] = 'a';
	}
}
 
int main()
{
	char string[5000];	
	int ch;
	printf("Enter a string:\t");
	scanf("%s", string);
	printf("\nString:\t%s\n",string);
	encrypt(string);
	printf("\nEncrypted String:\t%s\n", string);
	decrypt(string);
	printf("\nDecrypted string:\t%s\n", string);
	return 0;
}