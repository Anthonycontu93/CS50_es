#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
  long creditCardNumber;

  do
  {
    creditCardNumber= get_long("Input your card number:\n");
  }
  while(creditCardNumber<=0);

 long checkValidCard = creditCardNumber;
 int sum;
 int counter =0;
 long divisor = 10;
 char result[12];

//first case get the last number and sum

 while(checkValidCard >0)
 {
  int lastDigit = checkValidCard %10;
  sum = sum + lastDigit;
  checkValidCard = checkValidCard / 100;

 }

//second case get the secodn last number and mult
 checkValidCard = creditCardNumber/10;

while(checkValidCard >0)
 {
  int lastDigit = checkValidCard %10;
  int TimesTwo = lastDigit * 2;
  sum = sum + (TimesTwo % 10) + (TimesTwo/10);
  checkValidCard = checkValidCard / 100;

 }

// find the lenght of the number
 checkValidCard = creditCardNumber;
 while(checkValidCard > 0)
 {

  checkValidCard = checkValidCard/ 10;
  counter++;
 }

//get the divisor to divide and firstDigits

  for (int i=0; i< counter -2; i++)
  {
    divisor = divisor *10;
  }
  int firstDigit = creditCardNumber /  divisor ;
  int firstTwoDigit = creditCardNumber / (divisor /10);

  // check final
  if (sum % 10 == 0)
  {
    if (firstDigit ==4 && (counter==13 || counter == 16))
    {
       strcpy(result, "VISA");
    }
    else if((firstTwoDigit == 34 || firstTwoDigit==37) && counter ==15)
    {
      strcpy(result, "AMEX");
    }
    else if ((50 > firstTwoDigit || firstTwoDigit < 56) && counter ==16)

    {
      strcpy(result, "MASTERCARD");

    }

    else
    {
      strcpy(result, "INVALID");
    }

  }
  else
  
    {
     strcpy(result, "INVALID");
    }

    printf("%s\n", result);

}





