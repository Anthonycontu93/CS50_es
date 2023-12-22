#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)

{

 char n;
 char y;
 char go_on;
 long CardNumber[16];
 long cc [16];
 long checkCardNumber;

label1: do
 {
  CardNumber = get_string("Input cc:");
  printf("Output: ");
 }while(CardNumber<=0);


 for (int i=0; i< strlen(CardNumber); i++)
 {

  printf("%c", (int) CardNumber[i]);

  for(int j=0;j<strlen(CardNumber);j++)
  {
     scanf("%ld", &cc[j]);
  }
 }

 printf("\n");
 go_on = get_char("Is the cc correct?:Enter y or n\n");

 if(go_on == 121)

 {

  // first case get the second number


  if(strlen(CardNumber)>13)
 {
    printf("Visa");
 }

 if(go_on == 110)
 {
    goto label1;
 }

 }


 printf("\n");





}