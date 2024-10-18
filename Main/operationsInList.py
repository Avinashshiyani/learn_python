my_list = [10, 20, "hello", "world", 10.20]  # Original list

# Print the list
print("Original List:", my_list)

# Append a new element to `my_list`
my_list.append("Hello")  # Appending a new element
print("After Appending:", my_list)

# Remove an element from `my_list`
my_list.remove("hello")  # Removing an element
print("After Removing 'hello':", my_list)

# Check if a specific element is in `my_list`
hasElement = 1 in my_list 
print("Is 1 in my_list?", hasElement)

# Sort `my_list` in ascending order
numeric_list = [10, 20, 10.20]
numeric_list.sort()
print("Sorted numeric list:", numeric_list)

# Reverse the order of elements in `my_list`
my_list.reverse()
print("Reversed List:", my_list)
