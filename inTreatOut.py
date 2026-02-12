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

# Question 5. Calculate a square's area
# side = float(input("Inform the square's side length: "))
# print(f"That square has a area of {side ** 2} area.")

# Question 6. Ask for User's pay per hour and how much hours he works per month, then print hers/his monthly pay
# pay_hour = float(input("How much are you paid per worked hour? "))
# hours_month = float(input("And how many hours do you work per month? "))
# print(f"Your monthly pay is R$ {pay_hour * hours_month : .2f}.")

# Question 7. Knowing someone's height, calculate that person's ideal weigth for a woman (62,1 * HEIGHT - 44,7) and a man (72,7 * HEIGHT - 58)
# height = float(input("Please state your height: "))
# w_woman = 62.1 * height - 44.7
# w_man = 72.7 * height - 58.0
# print(f"If you are a woman, you ideal weigth is {w_woman : .2f}.\nIf you are a man, you ideal weigth is {w_man : .2f}.")

# Question 8. Ask for User's pay per hour and how much hours he works per month, calculate and print hers/his monthly brute pay, discount 11% for IR,
# 8% for INSS and 5% for worker's union. Finally, show the liquid pay.

# pay_hour = float(input("How much are you paid per worked hour? "))
# hours_month = float(input("And how many hours do you work per month? "))

# brute_pay = pay_hour * hours_month
# d_IR = brute_pay * 0.11
# d_INSS = brute_pay * 0.08
# d_UNION = brute_pay * 0.05
# liquid_pay = brute_pay - d_IR - d_INSS - d_UNION

# print(f"+ Brute pay R$ {brute_pay : .2f}.")
# print(f"- IR discount R$ {d_IR : .2f}.")
# print(f"- INSS discount R$ {d_INSS : .2f}.")
# print(f"- UNION discount R$ {d_UNION : .2f}.")
# print(f"= Brute pay R$ {liquid_pay : .2f}.")

# Question 9. Ask for the User's monthly salary and the minimum salary, then calculate and print how much times he earns the minimum salary
# salary_user = float(input("Inform your monthly salary: "))
# salary_minimum = float(input("Inform the minimum salary: "))
# print(f"You earn {salary_user/salary_minimum : .2f}x the minimum salary.")

# Question 10. Ask for the User's original debt (PRESENT VALUE), monthly rate and the number of months for complete payment,
# then calculate the total that was paid (FUTURE VALUE). P.S.: use simple interest.
# pv = float(input("How much was the loan worth? "))
# i = float(input("How much was the monthly interest? ")) / 100.0
# n = float(input("How many months to complete payment? "))
# fv = pv + (pv * i * n)
# print(f"\nYou paid R$ {fv : .2f} for a R$ {pv : .2f} loan in simple interest.")
# # EXTRA! Value for compound interest
# fv2 = pv * ((1 + i) ** n)
# print(f"Luckly you didn't paid R$ {fv2 : .2f} from compounded interest.")