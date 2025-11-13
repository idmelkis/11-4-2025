# 2. Uzdevums (2p)
# Izstrādājat programmu, kas izvada katru trešo skaitli no 1 (ieskaitot) līdz n (n ir lietotāja ievadīts skaitlis, kam ir jābūt mazākam par 1000), un to reizinājumu.
# Ja lietotāja ievadītais skaitlis lielāks par 1000, vai mazāks par 1, programma beidz darbu izvadot kļūdas ziņojumu.
# Piezīme: Izmantojot range, parametri ir (sākums, beigas, solis).
# n = int(input("Skaitlis no 1 līdz 1000: "))
# if n < 1 or n > 1000:
#     print("Kļūda: skaitlis nav diapazonā")
# else:
#     reizinājums = 1
#     for iii in range(1, n + 1, 3):
#         print(iii, end = " ")
#         reizinājums = reizinājums * iii
#     print()
#     print(reizinājums)

# Piemērs:
# f(x) = x^2
# Funkcijas definīcija
def kvadrats(x):
    return x * x # Atgriež x ^ 2
print(kvadrats(2))
print(kvadrats(4))
print(kvadrats(8))
mainigais = kvadrats(6)
print(mainigais)

def funkcija(x, y, z):
    print(x, y, z)
funkcija(1, 2, 3)
print(funkcija(1,2,3))
#funkcija(1,2) # Būs kļūda

def funkcija2(x, y, z = 10): # Standarta vērtība
    print(x, y, z)
funkcija2(x=10, y=20)

def funkcija2(x, y, z):
    print(x, y, z)
#funkcija2(10, 20)

def funkcija2(*x):
    print(x)
    # x[0] = 1 # Nestrādās - x ir tuple - saraksts, kas neļauj mainīt vērtības
    print(x[5])
funkcija2(15,14,321,4023,432,44,99)

def funkcija(*x, parametrs="99"):
    print(parametrs)
funkcija(10, 20, 30, 40, parametrs="101")
# Print strādā līdzīgi augstāk definētajai funkcijai - bezgalīgi daudz vērtības ar *values, un ir parametrs (end), kuru varam norādīt ar nosaukumu.
print(10,20,30,40,50,60, end=" ")
print(10,20,30,40)

def funkcija_ar_typedef(x :int, y :float, z :str, a: 'list[int]') -> float:
    """
      Šeit ir komentārs kas parādās uzliekot peli virsū funkcijai!
    """
    return x*z
#funkcija_ar_typedef(0)

# Nav gluži atbilstošs - pieņem sarakstu, nevis neierobežotu daudzumu param. (skaitļus)
# def lielakais_skaitlis_saraksts(skaitli :list[int]) -> int:
#     """Izvada lielāko skaitli no parametriem"""
#     lielakais_skaitlis = skaitli[0]
#     for skaitlis in skaitli:
#         if skaitlis > lielakais_skaitlis:
#             lielakais_skaitlis = skaitlis
#     return lielakais_skaitlis
# print(lielakais_skaitlis_saraksts([0, 10, 20, 30, 99, 10]))
# print(lielakais_skaitlis_saraksts([9, 34, 4]))
# print(lielakais_skaitlis_saraksts(654, 23, 999))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada lielāko skaitli
# Neizmantot iebūvētās python matemātiskās funkcijas (max())
def maks_skaitlis(*skaitli: tuple[int]) -> int:
    """Izvada lielāko skaitli no parametriem"""
    lielakais_skaitlis = skaitli[0]
    for skaitlis in skaitli:
        if skaitlis > lielakais_skaitlis:
            lielakais_skaitlis = skaitlis
    return lielakais_skaitlis

print(maks_skaitlis(0, 10, 20, 30, 99, 10))
print(maks_skaitlis(9, 34, 4))
print(maks_skaitlis(654, 23))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada šo skaitļu reizinājumu
def reizinajums(*skaitli: tuple[int]) -> int:
    reizinājums = 1
    for iii in skaitli:
        print(iii, end = " ")
        reizinājums = reizinājums * iii
    print()
    return reizinājums
print(reizinajums(1, 4, 7, 10))
