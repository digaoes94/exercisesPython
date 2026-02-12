# Question 1. Ask the User for a number, read it and then print "The chosen number was:"
# number = float(input("Type a number, whole or broken\n"))
# print(f"The chosen number was: {number}")

# Question 2. Ask for four grades and print the student's final grade
# finalGrade = 0.0; grades = 0

# finalGrade += float(input("Grade1: "))
# grades += 1
# finalGrade += float(input("Grade2: "))
# grades += 1
# finalGrade += float(input("Grade3: "))
# grades += 1
# finalGrade += float(input("Grade4: "))
# grades += 1
# print(f"Student's final grade = {finalGrade/grades}")

# REFINEMENT Question 2
x = 0; finalGrade = 0.0; grades = 0

for x in range(1, 5):
    finalGrade += float(input(f"Grade{x}: "))
    grades +=1

print(f"Student's final grade = {finalGrade/grades}")