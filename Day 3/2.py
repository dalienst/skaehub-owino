import numpy as np
def number_of_weekdays():
    this_month = str(input("Enter the month you want in the format yyyy-mm: "))
    next_month = str(input("Enter the next month in the format yyyy-mm: "))
    print("Number of weekdays in this month are: ", np.busday_count(this_month, next_month))

number_of_weekdays()