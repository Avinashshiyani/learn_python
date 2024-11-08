# 5. Write a python program to create dictionary called `student` with keys: "firstname",
# "lastname",”cmat” and "rollno" and fill in the values with your own information.
# a) Print the value associated with the "rollno" key.
# b) Add a new key-value pair to the dictionary, e.g., "city" and your city of residence.
# c) Remove the "cmat" key from the dictionary.
# d) Check if "city" is a key in the dictionary.
# Display appropriate results to verify the output.

student = {
    "firstname":"Avinash",
    "lastname":"shiyani",
    "cmat":False,
    "rollno":36,
}

# roll key print
print(student["rollno"])

# add city and city of refrence
student["city"] = "jamnagar"

# remove elemnt
student.pop("cmat")

# check if city
checkCity = "city" in student
print(checkCity)
print(student)