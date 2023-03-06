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