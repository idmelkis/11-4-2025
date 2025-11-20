# Uzdevums
# Ir definēta funkcija, ar kuru var ievadīt vairākus skaitļus sarakstā:
def skaitluIevade() -> 'list[int]':
    skaitli = []
    while True:
        ievade = input("Skaitlis:")
        if ievade.isdigit():
            skaitli.append(int(ievade))
        else:
            break
    return skaitli

# Jāuzraksta funkcija, kas saskaita skaitļu summu sarakstā un izsaucat to
# izmantojot funkcijas skaitluIevade rezultātu.
def saskaitisana(skaitli: list[int]) -> int:
    rezultats = 0
    for iii in skaitli:
        rezultats = rezultats + iii
    return rezultats

# 3 rindas
# ievaditie_skaitli = skaitluIevade()
# rezultats = saskaitisana(ievaditie_skaitli)
# print(rezultats)

# 1 rindā
# print(saskaitisana(skaitluIevade()))

# Rekursija: Funkcija, kas izsauc pati sevi:
# Piemērs: Funkcija izvada skaitļus no n (ievade) līdz 0 skaitot uz leju
def rekursija(parametrs):
    print(parametrs)
    if parametrs > 0:
        return rekursija(parametrs - 1)
    else:
        return parametrs # 0
rekursija(100)

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 0 līdz n (piem 3! = 1*2*3=6)
# n = int(input("Ievadat skaitli: "))
# rezultats = 1
# for skaitlis in range(1, n+1):
#     rezultats *= skaitlis # ekvivalents `rezultats = rezultats * skaitlis`
# vai ar while ciklu
# rezultats = 1
# while n > 0:
#     rezultats *= n
#     n -= 1
# Uzdevums - uzrakstīt funkciju, kas rekursīvi aprēķina faktoriāli
def faktorialis(skaitlis :int) -> int:
    if skaitlis == 1:
        return 1
    else:
        return skaitlis * faktorialis (skaitlis-1)
faktorialis(5)

# Vārdnīcas - 
saraksts = []
kortezs = () # Tuple - saraksts kuram nevar mainīt vērtības

# datu tips, kas līdzīgi, kā saraksti glabā vairākas vērtības
# dati tiek glabāti formātā - atslēga<->vērtība
# piemērs - datu bāzes
mainīgais = 234 # definējot vārdnīcu var izmantot mainīgos - tiks izmantota tā vērtība
vārdnīca = {
    'atslēga': 'vērtība',
    123: 'cita vērtība',
    mainīgais: 'vēl cita vētība',
    # atslēgas neva sākties ar skaitļiem, spec. simboliem (piem. !)
}
print(vārdnīca['atslēga'])
print(vārdnīca[123])
print(vārdnīca[mainīgais])
print(vārdnīca[234])

# Piemērs: Izmantot vārdnīcas lai pārveidotu tekstā burtus āēīū formā bez
# garumzīmes, t.i. aeiu
burti = {
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ū": "u",
    "š": "s"
}
def changeLetter(text :str, burti : 'dict[str, str]') -> str:
    """
    Funkcija iet pāri tekstam katram burtam, un pārbauda, vai burts ir vārdnīcā
    """
    result = ""
    for letter in text:
        if letter in burti: # Pārbauda, vai vārdnīcā eksistē atslēga - tekošais burts
            result += burti[letter]
        else:
            result += letter
    return result
print(changeLetter("Māja", burti))
print(changeLetter("Vējš", burti))
print(changeLetter("Vētra", burti))

# Piekļūšana vērtībām
print(burti.keys())
print(burti.values())
for atslēga, vērtība in burti.items():
    print(f"atslēga: {atslēga}, vērtība: {vērtība}")

# Nāk. stundā - vēlreiz šis + datu pievienošana vārdnīcai