# Question 1. Create a tuple with the 20 top ranked soccer teams from the 2020 Brazilian Soccer Championship, and then:
# a) Show top 5; b) Show last 4; c) Show teams in alphabetic order; d) Show São Paulo's position
# campeonatoBR_2020 = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense",
#                       "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Red Bull Bragantino",
#                         "Ceará", "Corinthians", "Atlético Goiense", "Bahia", "Sport",
#                           "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo"
#                     )

# print("=====  Top 5 teams  =====")
# a = 0
# while a < 5:
#     print(campeonatoBR_2020[a])
#     a += 1

# print("\n=====  Last 4 teams  =====")
# a = len(campeonatoBR_2020)- 4
# while a < 20:
#     print(campeonatoBR_2020[a])
#     a += 1

# print("\n=====  Alphabetical Order  =====")
# sorted = tuple(sorted(campeonatoBR_2020))
# for x in sorted:
#     print(x)

# print("\n=====  São Paulo's position  =====")
# try:
#     print(f"São Paulo's position was {campeonatoBR_2020.index("São Paulo") + 1}.")
# except:
#     print("São Paulo wasn't in the top 20.")

# Question 2. Read 4 integer numbers, add them to a tuple and then print:
# a) how many times the n9 appears in the tuple; b) the index from the first n3; c) which numbers are odd
# aList = []; odds = []; a = 1

# while a < 5:
#     print(f"Inform number {a}: ")
#     x = int(input())

#     if (x % 2) == 0:
#         odds.append(x)
    
#     aList.append(x)
#     a += 1

# aTuple = tuple(aList)

# print("\n=====  N° of time the number 9 appears  =====")
# n9 = aTuple.count(9)
# print(f"The number 9 appears {n9} times within the tuple")

# print("\n=====  Index from first occurence from the number 3  =====")
# n3 = 0
# try:
#     print(f"First occurence of number 3 happens at index {aTuple.index(3)}")
# except:
#     print("The number 3 doesn't appear within the tuple")

# print("\n=====  Odd numbers  =====")
# for x in odds:
#     print(x)

# Question 3. Create a program where the User can provide N numbers and insert those in a list. If the number already exists in the list, do not add it.
# After all N numbers where informed, print them in ascendent manner.

# n = int(input("How many numbers will you digit?"))
# list = []

# for m in range(n):
#     x = int(input(f"Inform the number {m+1}: "))

#     if x not in list:
#         list.append(x)
    
#     m += 1

# list.sort()

# for x in list:
#     print(x)

# Question 4. Create a program where the User can provide N numbers and insert those in a list, and then: a) print de numbers in decrescent order;
# b) if the number 5 is in the list

n = int(input("How many numbers will you digit? "))
list = []

for m in range(n):
    x = int(input(f"Inform the number {m+1}: "))
    list.append(x)
    m += 1

list.sort(reverse = True)
for x in list:
    print(x)

if 5 in list:
    print("5 is in the list")
else:
    print("5 isn't in the list")
