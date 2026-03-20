mainīgais = "vērtība"

# Datu glabāšana uz diskiem: https://en.wikipedia.org/wiki/Disk_sector
# Windows failu sistēma: https://en.wikipedia.org/wiki/NTFS
# C:\Mape1\Fails.txt
# /var/log/log.txt

# Absolūtais Ceļš
# Ceļš sākot no diska sākuma līdz failam vai mapei
# C:\Users\idmelkis\Desktop\11d\20_nodarbiba.py

# Relatīvais Ceļš
# Papildus informācija: https://www.lenovo.com/au/en/glossary/relative-path/
# Fails uz desktopa - strādājām mapē "11d" kas atrodas uz desktop
# Slīpsvītras - Windows māk gan uz priekšu (/), gan aizmuguri (\), bet izmantojot
# python str, slīpsvītras uz aizmuguri vajag dublēt (\\), t.i.
# .\\ = pašreizējā mape
# ..\\ = iepriekšējā mape
# ..\\.. = Mape virs iepriekšējās mapes
# .\11d\20_nodarbiba.py

import os
# N.B. Uz servera Python failus nemācēs atrast
print(os.getcwd()) # Parāda kur ir palaista programma
# isfile - pārbauda _faila_ eksistenci
print(os.path.isfile("C:\\Users\\idmelkis\\Desktop\\11d\\20_nodarbiba.py"))
print(os.path.isfile(".\\11d\\20_nodarbiba.py"))
print(os.path.isfile("..\\6_KD3.txt"))
print(os.path.isfile("..\\11d\\..\\6_KD3.txt"))
print(os.path.isfile("C:\\Users\\idmelkis\\Desktop\\11d\\..\\11a\\README.MD"))

# isdir - pārbauda _mapes_ eksistenci
print(os.path.isdir("..\\11d"))
print(os.path.isdir("C:\\Users\\idmelkis\\Desktop\\11d"))

# exists - pārbauda _ceļa_ eksistenci
print(os.path.exists("C:\\Users\\idmelkis\\Desktop\\11e")) # false - neeksistē
print(os.path.exists("C:\\Users\\idmelkis\\Desktop\\11d\\README.MD")) # eksistē
print(os.path.exists("C:\\Users\\idmelkis\\Desktop\\11d")) # eksistē

# Izvada pašreizējā faila atrašanās vietu
print(__file__)
faila_mape = os.path.dirname(__file__)
print(faila_mape)
os.chdir(faila_mape)
print(os.getcwd())
print(os.path.isfile(".\\20_nodarbiba.py")) # Būs patiess!

# Copy-paste variants lai nomainītu mapi
os.chdir(os.path.dirname(__file__))

# Alt veids - Palaižot var būt relatīvs ceļš - neiesaku, jo ceļš var būt relatīvs
#import sys
# Parametri - informāija kas tiek padota programmai palaižot to
# piem python .\20_nodarbiba.py --help
#print(sys.argv[0])
#print(sys.argv[1])
# izvadīs 
# .\20_nodarbiba.py
# --help

# Nākošajā stundā - failu izveide, rakstīšana, atvēršana u.t.t.