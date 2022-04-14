#CHECKING LEAP YEAR
year = int(input('Enter year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print(True)
    else:
        print(False)
elif year % 4 == 0:
    print(True)
else:
    print(False)
