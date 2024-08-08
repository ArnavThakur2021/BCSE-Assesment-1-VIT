""" A-23:- The Head Librarian at a library wants you to make a program that
calculates the fine for returning the book after the return date. You are
given the actual and expected return dates. Calculate the fine as
follows:
a. If the book is returned on or before the expected return date, no
fine will be charged; in other words, the fine is 0.
b. If the book is returned in the same month as the expected return
date, Fine = 15 Rupees × Number of late days
c. If the book is not returned in the same month but in the same year
as the expected return date, Fine = 500 Rupees × Number of late
months
d. If the book is not returned in the same year, the fine is fixed at 10000
Rupees."""



from datetime import date
def calculate_fine(actual_return, expected_return):
    if actual_return <= expected_return:
        return 0
    elif actual_return.year == expected_return.year:
        if actual_return.month == expected_return.month:
            return 15 * (actual_return.day - expected_return.day)
        else:
            return 500 * (actual_return.month - expected_return.month)
    else:
        return 10000
actual_day, actual_month, actual_year = map(int, input("Enter the actual return date (DD MM YYYY): ").split())
expected_day, expected_month, expected_year = map(int, input("Enter the expected return date (DD MM YYYY): "))
actual_return = date(actual_year, actual_month, actual_day)
expected_return = date(expected_year, expected_month, expected_day)

fine = calculate_fine(actual_return, expected_return)
print(f"The fine is: {fine} Rupees")