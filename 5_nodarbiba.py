# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 0 līdz n (piem 3! = 1*2*3=6)
# n = int(input("Ievadat skaitli: "))
# rezultats = 1
# for skaitlis in range(1, n+1):
#     # print(f"*{skaitlis}", end="") # end="" - nākošais print paliks tajā pašā rindā
#     rezultats *= skaitlis # ekvivalents `rezultats = rezultats * skaitlis`
# print(f"={rezultats}")

# Uzdevums:
# Uzrakstīt programmu, kurā lietotājs ievada skaitli, un programma
# izvadīs rindas ar asteriskiem (*) - sākot ar vienu asterisku pirmajā
# rindā un par vienu vairāk katrā nākošajā
# piem. ievade 4
# Izvade:
# *
# **
# ***
# ****
# skaitlis = int(input("Ievadat skaitli"))
# # versija ar for
# for i in range(1, skaitlis+1):
#     print(i * "*")
# # alt versija ar while
# skaititajs = 0
# while skaititajs < skaitlis:
#     skaititajs += 1
#     print(skaititajs * "*")

# Uzdevums: Izveidot 5x5 reizināšanas tabulu
# Hint - cikls ciklā, 2x for 
# 1 2 3
# 2 4 6
# 3 6 9
for x in range(1, 6):
    for y in range(1, 6):
        # end - pēc print netiks pievienota jauna rinda
        print(x*y, end=" ")
    print()


# Uzdevums:
# Uzrakstīt ciklu [for], kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Ja skaitlis dalās ar 3 UN 5, izvada "FizzBuzz"
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat šo skaitli
# Dalīšanas atlikuma pārbaudei izmatot - % - modulus operatoru
# Modulus operators - izvada dalīšanas atlikumu, piem.
# 5 % 2 == 1
# 7 % 3 == 1
# Šo var izmantot lai pārbaudītu, vai skaitlis dalās ar
# citu skaitli (izvadīs 0).
# 6 % 3 == 0
# N.B. šī ir darbība - tā pat kā citas (saskaitīšana, reizināšana utt.)
# Lai pārbaudītu vērtību ir jāizmanto ==, >, < u.tt.
