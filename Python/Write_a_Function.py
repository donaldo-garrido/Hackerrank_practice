# Challenge: Write a Function


# TASK:

# Given a year, determine whether it is a leap year. 
# If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
# It is only necessary to complete the is_leap function. 

import math

def is_leap(year):
    leap = False
    
    # Write your logic here
    if  math.fmod(year, 4) == 0:
        leap = True
        if math.fmod(year, 100) == 0:
            leap = False
            if math.fmod(year, 400) == 0:
                leap = True
    return leap

year = int(input())