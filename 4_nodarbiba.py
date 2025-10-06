# Uzdevums:
# Uzrakstat for ciklu, kas izvada skaitļus no 0 līdz 10, izlaižot skaitļus 4 un 6.
# for skaitlis in range(0,11):
#     if skaitlis == 4 or skaitlis == 6:
#         continue # Izlaižam iterāciju
#     print(skaitlis)

# Uzdevums: Uzrakstīt šo for ciklu kā while ciklu
# skaitlis = 0
# while skaitlis < 11:
#     if skaitlis == 4 or skaitlis == 6:
#         skaitlis = skaitlis + 1
#         continue # Izlaižam iterāciju
#     print(skaitlis)
#     skaitlis = skaitlis + 1

# Uzdevums - uzrakstat ciklu (pēc izvēles) kas saskaita visas vērtības sarakstā,
# un jāizvada rezultāts. Neizmantot funkciju sum() (!)
saraksts = [ 0, 5, 4, 10, 9 ]

skaititajs = 0
for i in saraksts:
    skaititajs += i
print(skaititajs)

# VAI

skaititajs = 0
idx = 0
while idx < len(saraksts):
    skaititajs += saraksts[idx]
    idx += 1
print(skaititajs)

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 0 līdz n (piem 3! = 1*2*3=6)
# Nākošajā stundā