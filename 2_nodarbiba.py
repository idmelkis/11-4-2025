# Saraksti
saraksts = [ 0, 3, 4, 5 ]
# Mainīt vērtību
saraksts[1] = 7 # 3 => 7
print(saraksts)
# Pievienot vērtību
saraksts.append(10) # Beigās
print(saraksts)
# VAI
saraksts.insert(0, 50) # Sākumā (idx 0)
print(saraksts)
# Dzēst vērtību
saraksts.pop(3) # Skaitlis 4
print(saraksts)

# Ievade
#str(input("Ievade: ")) == input("Ievade: ") -- str sākumā nevajag(!) pievienot
# ievade = input("Ievade: ")
# print(2 + int(ievade)) # Uzmanību - burtus nevar pārveidot par skaitļiem (!)
#rezultāts = int("1") + 1

# Uzdevums: Lietotājam jāievada vērtība sarakstā
# saraksts = []
# saraksts.append(input("Ievade: "))
# print(saraksts)
#saraksts = [input("Ievade: "), input("Ievade: ")]

# If/elif/else
#patiesība = 1 == 2
if 1 == 1 and 2 == 2: # And izpilās tikai ja abi izpildās (patiesa)
    print("Izpildās")
if 1 == 1 or 2 == 3: # Or izpildās ja viena pārbaude izpildās (patiesa)
    print("Izpildās")

mainīgais = 1
if mainīgais == 1:
    print("Izvadam vienu lietu")
elif mainīgais == 2:
    print("Izvadam citu lietu")
else:
    print("Ja neizpildās neviens iepriekšējais if (vai elif)")

# Loģiskās pārbaudes
# == - Vienāds ar (pārbauda vērtības)
# is - Vienāds ar (pārbauda vērtības UN datu tipus)
# != - Nav vienāds ar
# not - Apgriež nākošo rezultātu
# > - Lielāks par ( 10 > 10 == False )
# < - Mazāks par
# >= - Lielāks vai vienāds par ( 10 >= 10 == True)
# <= - Mazāks vai vienāds par

# Uzdevums: Izveidot programmas izvēlni
# Lietotājs ievada skaitli, un programma
# Izvada - 
# Ja ievade ir 1, tad tiek izvadīts "Sveiks!"
# Ja ievade ir 2, tad tiek izvadīts autora vārds!
# Ja ievade ir 3, programma darbību beidz (funkcija quit())
print("Izvēlne --")
print("1. Sveicinājums")
print("2. Autora informācija")
print("3. Beigt darbu")
ievade = input("Ievade: ")
if ievade == "1":
    # Uzdevums: Lietotājs ievada vārdu, izvada "Sveiks {vārds}"
    vārds = ievade("Vārds: ")
    print(f"Sveiks {vārds}!")
    # VAI print(f"Sveiks", vārds, "!")
elif ievade == "2":
    print("Autors: ...")
elif ievade == "3":
    quit()
else: # Ja neatbilst
    print("Nepareiza ievade")

# Python 3.10+ - match jeb (citās prog. valodās) switch
# Viens mainīgais tiek pārbaudīts ar dažādām vērtībām
# match ievade:
#     case "1":
#         print("1. Sveicinājums")
#     case "2":
#         print("Autors: ...")
#     case "3":
#         quit()
#     case _: # Ja neatbilst
#         print("Nepareiza ievade!")
