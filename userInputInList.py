# 9. Write a python program to accept new value from the user and replace specific index in
# your list with new value. 

userInput = input("Enter input to replace")

list = ["hello" , "name" , "world"]

for i in range(len(list)):
    if list[i] == "name":
        list[i] = userInput

print(list)