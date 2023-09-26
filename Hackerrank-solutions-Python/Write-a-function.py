# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.



def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 ):
         leap = True;
         
    if (year % 100 == 0 and year % 400 == 0 ): 
        return True;
        
    if (year % 100 == 0):
        return False;
    
    if (year % 100 == 0 and year % 400 == 0 and year % 4 == 0):
        return True;
    
    return leap

year = int(input())
print(is_leap(year))