# 7
# Write a python program to create dictionary called ‘student’ and create Pandas dataframe
# from that dictionary. Display appropriate output.

import pandas as pd

student = {
    "name":["avinash"],
    "language":["english"],
    "coding":["python"],
}

useDataSet = pd.DataFrame(student)

print(useDataSet)
