# 3
# Write a python program to create a tuple called ‘months’ containing the names of the any
# ten months of the year. Perform following operations on the ‘months’ tuple.
# a) Print the fifth month.
# b) Print the last 2 months.
# c) Check whether ‘October’ is in the list or not.
# d) Try to add a new month to the tuple (#this should result in an error)
# e) Convert the tuple into a list, add remaining months, and then convert it back to a
# tuple. 

months = ("jan" , "feb" , "march" , "april" , "may","june" , "july","august" , "november" , "december" )

# print fifth elemnt
print(months[4])

# print last two months
print(months[-2:])

# octomber in therre or not
is_month_there = "october" in months
print(is_month_there)

# add new month
# addNewMonth = months.append("avinash")

# print(addNewMonth)

convert = list(months)

convert.append("avinash")

print(type(convert))

print(convert)