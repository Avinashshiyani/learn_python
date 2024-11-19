#16 Write a python program to create a new set with unique elements from both the sets by
# removing duplicate elements.

my_set = {"hello" , "world" , "my" , "name" , "is", "avinash"}
my_set_two = { "my" , "name" ,  "is" , "not" , "avinash"}

# union from makeing difference

difference = my_set.union(my_set_two);

print(difference)