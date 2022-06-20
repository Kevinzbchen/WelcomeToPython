import sys
import xml
import numpy
import pip
import datetime
from QuantLib import *

#little game -- guessing the number
import random as rand
number = rand.randint(1,99)
guess_num = int(input("Try any number between 1 - 99: "))
while number != guess_num:
    if number > guess_num:
        guess_num = int(input("The number is bigger than your guess, try again: "))
    else:
            guess_num = int(input("The number is smaller than your guess, try again: "))
print("CONGRATULATIONS!! YOU GOT IT!! The number is ", number)




