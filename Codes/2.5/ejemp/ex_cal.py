#!/usr/bin/env python 

# Python program to display calendar of given month of the year

import calendar

# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

