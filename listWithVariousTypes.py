# 1
# Write a python program to create a list of 12 elements containing various data types.
mylist = [9, 3.14, "gls", True, [1, 2, 3], (1,2,3), {1,2,3}, {"name": "jatin"}, None, 2+3j]

for i in mylist:
    print("element = " ,  i , "type = " , type(i))