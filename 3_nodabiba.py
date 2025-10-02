# Uzdevums 1:
# Ievade: Skaitlis
# Izvade: "Jā", ja skaitlis ir lielāks par 10, "Nē" ja ir mazāks
# ievade = int(input("Skaitlis: "))
# if ievade > 10:
#     print("Jā")
# else:
#     print("Nē")

# Uzdevums 2:
# Ievade: Jebkāds teksts
# Izvade: Šī teksta 1, 3 un 5 burts. Jāveic pārbaude vai ir tik garš teksts.
# ievade = input("Ievade: ")
# if len(ievade) >= 5:
#     print(f"{ievade[0]};{ievade[2]};{ievade[4]}")

# Uzdevums 3: Kalkulators
# Ievade: Skaitļi (vismaz 2), Darbība (*, /, +, -)
# Izvade: Darbības rezultāts
# skaitlis = input("Skaitlis 1:")
# skaitlis2 = input("Skaitlis 2:")
# darbiba = input("Darbība:")

# if skaitlis.isnumeric() and skaitlis2.isnumeric(): # Pārbauda vai ir ievadīts skaitlis
#     if darbiba == "*":
#         print(int(skaitlis) * int(skaitlis2))
#     elif darbiba == "/":
#         print(int(skaitlis) / int(skaitlis2))
#     elif darbiba == "+":
#         print(int(skaitlis) + int(skaitlis2))
#     elif darbiba == "-":
#         print(int(skaitlis) - int(skaitlis2))
# else:
#     print("Nav ievadīts skaitlis!")

# while
# while <darbība, kura atgriež True vai False>:
#     <komandas>
# pārbaude = 1 == 1
# print(pārbaude)
# while pārbaude:
#     print("Nebeidzas!")
#     pārbaude = False
# skaitlis = 0
# while skaitlis < 10:
#     skaitlis += 1 # skaitlis = skaitlis + 1
#     if skaitlis == 3:
#         continue # Beidz pašreizējo cikla iterāciju
#     if skaitlis == 8:
#         break # Pārtrauc ciklu
#     print(skaitlis)
    
# for
# saraksts = [0,1,4,7,3]
# for mainīgais in saraksts:
#     print(mainīgais)
# for indekss in range(1,11): # Izvada skaitļus no 1 līdz 11
#     print(indekss)
    # Strādā arī break un continue
# Ekvivalents
# indekss = 1
# while indekss < 11:
#     print(indekss)
#     indekss += 1

# Piemērs - vērtības atrašana sarakstā
# Jāatrod indekss vērtībai 3
saraksts = [1, 5, 7, 4, 3, 9]
for idx in range(len(saraksts)): # Range no 0 līdz saraksta garumam - piem., ja garums ir, tad idx būs 0,1,2,3
    if saraksts[idx] == 3:
        print(idx)
        break
idx = 0
while idx < len(saraksts):
    if saraksts[idx] == 3:
        print(idx)
        break
    idx += 1