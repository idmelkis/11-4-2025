# Nākošajā stundā - csv, mapes
# CSV - Comma separated values, parasti faila paplašinājums - .csv
# TSV - Tabulator separated values (tab poga)
# ;,| - arī var izmantot, ja nevar izmantot komatu
# Name,Age,City
# Anna,28,Riga
# Jānis,35,Liepāja
# Marta,22,Jelgava
with open("23_nodarbiba.csv", "r", encoding="UTF-8") as fails:
    # Atvēršanai - 
    # 1. Variants
    # Strādā, ja datos nav atdalītāja simbols (piem. komati)
    # izlaižam rindu - noder, ja gribam izlaist galveni
    # next(fails) 
    # for line in fails:
    #     # strip() - noņemam nevajadzīgos simbolus (\n)
    #     # split() - sadala tekstu sarakstā pēc noteikta simbola
    #     csv_rinda = line.strip().split(",")
    #     print(csv_rinda)
    # 2. Variants
    import csv
    # Jāizveido lasītājs
    # 1. param - fails vai saraksts ar tekstu kurā ir csv dati
    # 2. param - atdalītāja simbols (nav obligāti ja ir komats)
    # 3. param - pēdiņu simbols - lieto, ja datos parādās
    #            atdalītāja simbols
    lasitajs = csv.reader(fails, delimiter=",", quotechar='"')
    for line in lasitajs:
        print(line)
    fails.seek(0) # noresetojam faila kursoru
    # var noderēt - csv uz vārdnīcu
    vārdnīca = csv.DictReader(fails)
    for line in vārdnīca:
        print(line)

# Uzdevums:
# Atverat vietni https://www.lipsum.com/
# Nokopējat tekstu zem "The standard Lorem Ipsum passage, used since the 1500s"
# Saglabājat to failā
# Iekš pitona atverat šo failu, kā csv failu (atdalītājs - atstarpe)
# Izvadīt vārdu skaitu failā (len)
with open("lorem.ignored", "r", encoding="UTF-8") as fails:
    for line in fails:
        csv_rinda = line.strip().split(" ")
        print(len(csv_rinda))

# Failu un mapju izveide, dzēšana
# Piezīme - visām funkcijām parametrā pieņem gan relatīvos, gan absolūtos ceļus
# Piemēros ir izmantots relatīvais ceļš - mapē kurā atrodās šis .py fails!
import os
# Nodrošina, ka faili un mapes veido tur pat kur ir .py fails
os.chdir(os.path.dirname(__file__))
if not os.path.exists("ignored"):
    os.mkdir("ignored") # Izveido mapi
else:
    print("Mape eksistē!")

# 1. variants izdzēst mapi manuāli
# Iztīrīt mapi
# for fails in os.listdir("ignored"):
#     # Listdir nepievieno mapes nosaukumu pie faila - tas jādara manuāli
#     faila_pilnais_nosaukums = "ignored\\"+fails
#     os.remove(faila_pilnais_nosaukums)
# # Izdzēš mapi - strādā tikai, ja mape ir tukša
# os.rmdir("ignored")

# 2. variants - izdzēst visu automātiski
import shutil
shutil.rmtree("ignored")

# Uzdevums: Uzrakstat programmu kura izveido mapi "mape"
# Mapē izveidojat failus ar nosaukumiem no 1 līdz 100
if not os.path.exists("mape"):
    os.mkdir("mape") # Izveido mapi
for iii in range(0,101):
    with open(f"mape\\{iii}", "w", encoding="UTF-8") as fails:
        pass
import shutil
shutil.rmtree("mape")

# i/ni uzdevums:
# Dots fails 'cilvēki.csv' ar sekojošu tekstu: 
# Vārds,Uzvārds,Vecums
# Jānis,Bērziņš,17
# Marta,Liepiņa,18
# Pēteris,Ozols,19
# Anna,Kārkliņa,19
# Fails pieejams: https://ayy.lv/ini.csv
# Izveidojat programmu kas nolasa šo failu, un izvada datus sekojošā formātā:
# Vārds: <vārds>
# Uzvārds: <uzvārds>
# Vecums: <vecums>
# <jauna rinda>