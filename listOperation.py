# 4
# Write a python program to create two sets, `set1` and `set2`, containing some common
# and unique elements. Perform following operations.
# a) Display the number of elements of both the sets.
# b) Find the intersection of `set1` and `set2`
# c) Find the union of `set1` and `set2`.
# d) Check if `set1` is a subset of `set2`.
# e) Add an element to `set1` and remove an element from `set2`.
# Display appropriate results to verify the output.

set1 = {"hello" , "world"}
set2 = {"hello" , 2 , "world"}

# length of elemnts
print(len(set1))
print(len(set2))

# find the intersection
setIntersection = set1.intersection(set2)
print(setIntersection)

# find union 
findUnion = set1.union(set2);
print(findUnion)

# subset
findSubset = set1.issubset(set2)
print(findSubset)

addEle = set1.add("avinash")
delEle = set2.remove("world")
print(set1)
print(set2)