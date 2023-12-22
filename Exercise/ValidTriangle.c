#include <stdio.h>
#include <cs50.h>

bool valid_triangle (int a, int b, int c);
int main (void)
{

 int a,b,c;
 bool Triangle;

 a= get_int("Input a lenght:");
 b= get_int("Input a lenght:");
 c= get_int("Input a lenght:");

 Triangle= valid_triangle(a,b,c);

 if(Triangle)
 {
    printf("Correct, is valid!");
 }
 else
 {
    printf("Is not valid!");
 }


}



bool valid_triangle (int a, int b, int c)
{

 bool Triangle;

   if(a>0 && b>0 && c>0)
  {
    if((a+b)>c && (b+c)>a && (a+c)>b)
    {

       return Triangle=1;
    }
    else
    {
        return Triangle=0;
    }
   }
   else
   {
    return 0;
   }

 }


