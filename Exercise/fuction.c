#include <stdio.h>
#include <cs50.h>


float mult_float (float a, float b);

int main (void)
{

  float a,b,total;


  a=get_float("Give a number: ");

  b=get_float("Give a number: ");

  total= mult_float(a,b);

  printf("The result is: %f\n",total);
}


float mult_float (float a, float b)
{
    float tot;
    tot=a*b;
    return tot;
}