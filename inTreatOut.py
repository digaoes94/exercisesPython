import math
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
# x = 0; finalGrade = 0.0; grades = 0
# for x in range(1, 5):
#     finalGrade += float(input(f"Grade{x}: "))
#     grades +=1
# print(f"Student's final grade = {finalGrade/grades}")

# Question 3. Do a code that translates meters to centimeters
# meters = float(input("Inform how much meters: "))
# print(meters*100)

# Question 4. Do a code that asks for a circle's radius and show it's area
# radius = float(input("Inform the circle's radius: "))
# print(f"Circle's area is {math.pi * radius ** 2 : .4f}")

# Question 5. Ask for User's pay per hour and how much hours he works per month, then print hers/his monthly pay
# pay_hour = float(input("How much are you paid per worked hour? "))
# hours_month = float(input("And how many hours do you work per month? "))
# print(f"Your monthly pay is R$ {pay_hour * hours_month : .2f}.")

