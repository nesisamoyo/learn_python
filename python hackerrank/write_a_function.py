def is_leap(year):
    # leap = False sets default return value of leap for the function as Boolean value
    # which is set to False for now
    leap = False
    
    # Write your logic here
    # If it a leap year it should be evenly divisble by 4, not evenly divisible by 100
    # and evenly divisible by 400
    if (year % 4 == 0) and (year %100 != 0 or year %400 ==0):
        return True
        
    return leap

year = int(input())
print(is_leap(year))
