# Uzdevumi
# 1. Izvadi skaitu ar katru paplašinājumu failiem kādai lietotāja ievadītajai mapei
import os
# cels = input("Ievadat ceļu uz mapi ar failiem: ")
# # Iegūt failu sarakstu
# faili = os.listdir(cels)
# skaits = {}
# for fails in faili:
#     # Iegūt faila paplašinājumu
#     paplasinajums = fails.strip().split(".")[-1]
#     # Saskaitīt tos
#     skaits[paplasinajums] = skaits.get(paplasinajums, 0) + 1
#     # Jeb (garāks veids):
#     # if paplasinajums in skaits:
#     #     skaits[paplasinajums] = 1
#     # else:
#     #     skaits[paplasinajums] += 1
# print(skaits)

# 2. Izveidojat programmu, kas izvada vai lietotāja dotais ceļš ir fails vai mape
# Ja neeksistē - jāizvada, ka ceļš neeksistē
# cels = input("Ievadat ceļu uz mapi ar failiem: ")
# if os.path.isfile(cels):
#     print("Dots fails")
# elif os.path.isdir(cels):
#     print("Dota mape")
# else:
#     print("Ceļš neeksistē!")

# 3. Ir dots CSV fails - 
# [https://ayy.lv/11d.csv]
# Saturs:
# name,age,grade
# Alice,19,"[8,9,10,0]"
# Bob,20,"[9,10,4,4]"
# 1. Izvadīt vidējos vērtējumus katram cilvēkam.
import csv
import json
with open("24_nodarbiba.csv", "r", encoding="UTF-8") as fails:
    next(fails)
    reader = csv.reader(fails)
    vid_atzs = []
    for cilveks in reader:
        print(cilveks) # Saraksts - rinda no csv faila
        atzimes = cilveks[2] # Iegūstam trešo kolonu no CSV saraksta
        print(atzimes[3]) # Izvadīs trešo BURTU, jo trešajā kolonā bija teksts (pēdiņās)
        atzimes_sar = json.loads(atzimes) # Pārveido tekstu (starp kvadrātiekavām []) uz sarakstu 
        print(atzimes_sar)
        aritm_vid = sum(atzimes_sar) / len(atzimes_sar)
        print(aritm_vid) # Aritmētiskais vid.
        # 2. Izvadīt vidējo vērtējumu abiem cilvēkiem
        vid_atzs.append(aritm_vid)
    aritm_vid = sum(vid_atzs) / len(vid_atzs)
    print(aritm_vid) # Aritmētiskais vid.
    
    # 3. Izvadi visus datus JSON(!) formātā
    fails.seek(0)
    vārdnīcas = csv.DictReader(fails)
    for vardn in vārdnīcas:
        print(json.dumps(vardn))

# 4. Pievieno jaunu skolēnu šim failam!
with open("24_nodarbiba.csv", "a", encoding="UTF-8") as fails:
    vards = input("Vārds: ")
    vecums = int(input("Vecums: "))
    atzimes = [] # TODO: Vairākas atzīmes
    csv_str = f"{vards},{vecums},\"{json.dumps(atzimes)}\"\n"
    fails.write(csv_str)
    # otrs variants - izmantot csv bibliotēku
    # ...