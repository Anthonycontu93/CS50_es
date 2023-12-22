#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

bool only_digit(string k);
char rotate( char p, int k);

int main(int argc, string argv[])
{
 // c(i) = (p(i) + k)%26 formula per la criptazione
 // c è la lettera finale, p la posizione (i) la posizione futura e k la chiave di lettura

char c;
string p;
char final_sent[50];
int n, m;

if(argc == 2)
{

bool arg2 = only_digit(argv[1]);

if (!arg2)
{
   printf(" Usage: ./caesar key\n");
   return 1;
}
else

m = atoi(argv[1]);
p = get_string("plaintext:  ");
n = strlen(p);


for (int i=0; i<n; i++)
{
 c = rotate(p[i], m);
 final_sent[i] = c;
}
printf("ciphertext: %s\n", final_sent);


}
else if (argc > 2 || argc <= 1)
{
   printf(" Usage: ./caesar key\n");
   return 1;
}

}

bool only_digit(string k)
{
  int lenght;
  int i = 0;
  bool val;

  lenght = strlen(k);

  do
  {

   if ( k[i] >= 48 && k[i] <= 57 )
   {
    val = true;
    i++;

   }

   else
   {
    val = false;
    i = lenght;
   }
  } while (i < lenght );


 return val;

}

char rotate( char p, int m)
{
 int i;
 char final_w;

 for( i=0; i<m; i++)
 {
  if (p >= 32 && p < 65)
  {
    final_w = p;
  }
  else if (p >= 65 && p <= 90)
  {

    if( p + m > 90)
    {
      int s, k;
      s = (p + m) - 90;

       if(s > 25)
      {
        do
        {
          s = (s - 26);
          final_w = 65 + s;
        } while ( s > 25);

       k = 64 + s;
       final_w = k;
      }
    }
    else
    {
      final_w = ( p + m);
    }

  }
  else if (p >= 97 && p <= 122)
  {
      if( p + m > 122)
    {
      int s, k;
      s = (p + m) - 122;
      if(s > 25)
      
      {
        do
        {
          s = (s - 26);
          final_w = 96 + s;
        } while ( s > 25);

      }

      else
      {
       k = 96 + s;
       final_w = k;
      }

    }
    else
    {
       final_w = ( p + m);
    }

  }
  else
  {
    final_w = p;
  }
 }
 return final_w;
}