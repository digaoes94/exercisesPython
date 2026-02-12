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

