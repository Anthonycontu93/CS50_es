#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i,j,m,z=0,height;
    int counter,space;
   label1: do
    {
      height=get_int("How many briks?:");

      if(height>0 & height<9)
      {
        counter=1;
        space=height-1;
        for(i=0;i<height;i++)
        {
          for(j=0;j<space;j++)
          {
            printf(" ");
          }
          for(m=0;m<counter;m++)
          {
            printf("#");
          }
           space--;
           counter++;
           printf("\n");
           z++;
        }
      }
      else
      {
        goto label1;
      }
    }
    while(z<height);

}