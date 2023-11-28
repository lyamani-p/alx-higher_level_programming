#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit < 6 and digit!=0:
    print("less than 6 and not 0")
    
elif digit == 0:
    print("0")
else:
    print("greater than 5")
