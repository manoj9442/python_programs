#Take year from user to check leap year or not
year = int(input("Enter Year : "))
is_leap_year = False
#Check year is divisible by 4 or not
if year % 4 == 0:
    """check year is divisble by 100 then it must be divisble by 400
        for leap year
    """
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False
if is_leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")        
    