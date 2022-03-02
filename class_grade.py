
""" Plain English
Start
Create a list to store 5 numbers (float)
capture user's input 5 times for their grades
each time we capture the user's input, we append the number to the list
sort the list ascending, then splice the items starting at index 2
once we have three highest number in the list, we sum them up and divide by 3
output a message to the user 
end
"""

""" Psudocode
create list
capture input
append number to list 

do this five times 

sort the list, then splice then splice out the two lowest number
print message to user 

"""

# grades = []

# grade = input("Enter the first grade: ")
# grades.append(float(grade))

# grade = input("Enter the second grade: ")
# grades.append(float(grade))

# grade = input("Enter the third grade: ")
# grades.append(float(grade))

# grade = input("Enter the fourth grade: ")
# grades.append(float(grade))

# grade = input("Enter the fifth grade: ")
# grades.append(float(grade))

# grades.sort()

# grades = grades[2:]

# grades = sum(grades)

# result = grades / 3
# print("Average Grade is {0:.2f}%".format(result))
# print(grades, 'results', result)

""""
Code refactor using loop
"""

grades = []

for i in range(5):

    grades.append(float(input("Enter the grade: ")))

grades.sort()
grades = sum(grades[2:]) / 3
# grades = sum(grades)
# result = grades / 3

print("Average Grade is {0:.2f}%".format(grades))
print(grades, 'results')