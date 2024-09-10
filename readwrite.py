#!/bin/python3

months = open("months.txt")

# print(months)
# print(months.mode)
# print(months.readable())
# print(months.read())
# print(months.readline())
# print(months.readline())
# print(months.readlines())
# months.seek(0) # This will allow the lines to be read again
# print(months.readlines())

for month in months:
    print(month.strip())

months.close()