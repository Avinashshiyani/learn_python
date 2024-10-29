# 2
# Write a python program to create a list of cities and Perform following operations on the
# list of cities.
# a) Append a new city to the list.
# b) Print the first and last city in the list.
# c) Remove specific city from the list.
# d) Check whether ‘Amreli’ is in the list or not

my_city = ["jamnagar" , "rajkot" , "Ahmedabad"]

# a append city
my_city.append("surat")
print("append city" , my_city)

# b first and last city print
print("first element = " , my_city[0] , "last element =" , (my_city[-1]))

# c remove element
my_city.pop(-1)
print("removing last element ahmedabad = " , my_city)

checkCity = "amreli" in my_city
print ("check city" ,checkCity)