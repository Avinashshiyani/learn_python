# 21
# Write a Python program to check whether each number is a prime or not in a given list of
# numbers.

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True  

# Define a list of numbers to check
numbers = [2, 3, 4, 5, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]

# Check each number in the list
for num in numbers:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
