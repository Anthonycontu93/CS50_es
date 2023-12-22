#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes   (int cents);
int calculate_nickels (int cents);
int calculate_pennies (int cents);

int main(void)
{

    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - (quarters* 25);

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10);

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - (nickels * 5);

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - (pennies * 1);

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
    printf("%i 25c %i 10c %i 5c %i 1c\n",quarters,dimes,nickels,pennies);
 }

// fuction to get cent
int get_cents(void)
{
    int cents;
    label1: cents = get_int("How many cents owned?:\n");
    if(cents>=0)
    {
    return cents;
    }
    else
    {
        printf("Cents must be greater or equal to 0\n");
        goto label1;
    }

    printf("\n");
}

// calculete quaters
int calculate_quarters(int cents)
{
   int quarters = 25;
   int left_over = 0;
   int sum = 0;

   if (cents >= quarters)

   {
    do
   {

    left_over = cents - quarters;
    cents = left_over;
    sum++;

    } while (left_over >= quarters);


      cents = left_over;
      return sum;

   }
   else return sum;

}

// calculate dimes
int calculate_dimes(int cents)
{
   int dimes     = 10;
   int left_over = 0;
   int sum       = 0;

   if (cents >= dimes)

   {
    do
   {

    left_over = cents - dimes;
    cents = left_over;
    sum++;

    } while (left_over >= dimes);


      cents = left_over;
      return sum;

   }
   else return sum;
}

// calculate nickels
int calculate_nickels(int cents)
{
   int nickels   = 5;
   int left_over = 0;
   int sum       = 0;

   if (cents >= nickels)

   {
    do
   {

    left_over = cents - nickels;
    cents = left_over;
    sum++;

    } while (left_over >= nickels);


      cents = left_over;
      return sum;

   }
   else return sum;
}

// calculate pennies
int calculate_pennies(int cents)
{
   int pennies = 1;
   int left_over = 0;
   int sum = 0;

   if (cents >= pennies)

   {
    do
   {

    left_over = cents - pennies;
    cents = left_over;
    sum++;

    } while (left_over >= pennies);


      cents = left_over;
      return sum;

   }
   else return sum;

}
