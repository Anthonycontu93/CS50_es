import random
import sys


def main():

        # call get_int
        n = get_int()

        # get the number from the level input in get_int()
        number = random.randint(1, n)
        while True:
             try:
                  guess = int(input("Guess:"))
                  if guess <= n and guess >= 1:
                       break
             except:
                  continue

        if guess == number:
             sys.exit("Just right!")
        elif guess > number:
             print("Too large!")
        else:
             print("Too small!")



def get_int():


    while True:
        try:
             n = int(input("Level:"))
             if n >= 1:
                return n
             else:
                continue
        except ValueError:
             continue









main()