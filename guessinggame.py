#!/usr/bin/env python3
"""Player must guess a number between 1 and 100"""
import random

star= random.randint(1,100)
# generate a random number between 1 and 100
winner= ""

while winner != star:

    winner= int(input("pick a number between 1 to 100: "))
    # let the user type in input (guess a number)

    if winner < star:
        print("wrong, you are too low")

    elif winner > star:
        print("wrong, you are too high")

    else:
        print("you are a superstar")

    # the program will tell the user if:
      # they guessed it right
      # they guessed too low
      # they guessed too high

