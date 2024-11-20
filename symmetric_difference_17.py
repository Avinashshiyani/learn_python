#17
# Write a python program to demonstrate the difference and symmetric difference operation
# on two sets.
# [Symmetric difference contains elements that are in either of the sets but not in their intersection]
# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference = set1 - set2
symmetric_difference = set1.symmetric_difference(set2)

print("Difference (set1 - set2):", difference)
print("Symmetric Difference:", symmetric_difference)
