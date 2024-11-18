# 15. Write a python program to find the repeated items of a tuple
tup = ('a' , 'b' , 'z' , "1" , 'd' , 'e' , "1")
# finding repeated iteam
for i in tup:
    count = tup.count(i)
    if count > 1:
        print(f"{i} is repeated {count} times.")
