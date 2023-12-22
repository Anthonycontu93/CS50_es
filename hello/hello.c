
#include <stdio.h>
#include <cs50.h>

int main(void)

{
    //Var
    string answer;

    // Inputs name client
    answer = get_string("What is your name?");

    printf("Hello, %s\n", answer);
}
