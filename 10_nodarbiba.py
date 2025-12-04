vardnica = { 
    "atslēga": "vērtība",
    "val2": "vērt2"
}

# piekļūšana
print(vardnica["atslēga"]) # specifiska vērtība pēc atsl.
print(vardnica.keys()) # atslēgas kā saraksts
print(vardnica.values()) # vērtības kā saraksts
print(vardnica.items()) # atsl & vērtības kā saraksts - var lietot iekš for lai iegūtu abas vērt.

# datu ievietošana/atjaunināšana
vardnica.update({"jauna atsl": "jauna vērt"}) # Pievieno vai atjaunina atslēgu
vardnica["jauna atsl 2"] = "jauna vērt!"
print(vardnica)

# atjaunināšana
vardnica["jauna atsl 2"] = "jauna vērt!!!" # Ja atslēga sarakstā jau eksistē, tiek atjaunināta tās vērtība
print(vardnica)

# vērtību dzēšana no vārdnīcas - izdzēš atslēgu ar tās vērtību no vārdnīcas
vardnica.pop("jauna atsl") 
del vardnica["jauna atsl 2"] # del <vārdn. mainīgais>[<atslēga>]
print(vardnica)

# Uzdevums: (Dots) Tiek ģenerēts saraksts ar 20 vērtībām
# Ar ciklu izdzēst katru otro vērtību (atslēgas ir ar nepāra skaitļiem)
# Vārdnīcas garums - cik elementi (atslēgu-vērt pāri) ir vārdnīcā: len(vardnica)
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 1000)
print(vardnica)
print()
# Nestrādās - nedrīkst izmainīt vērtības, ja izmanto piekļūšanas funkcijas
# for key in vardnica.keys():
#     if key % 2 == 0:
#         del vardnica[key]
#         #vardnica.pop(key)
# Strādās, jo list atgriež jaunu sarakstu, kas nav saistīts ar vārdnīcu
# for key in list(vardnica.keys()):
#     if key % 2 != 0:
#         del vardnica[key]
#         #vardnica.pop(key)
# print(vardnica)
# Piemērs - izfiltrēt vērtības - pāra sk.
for key, value in list(vardnica.items()):
    if value % 2 != 0:
        del vardnica[key]
print(vardnica)

# mainīgais = 123
# atslēga: vērtība

# Uzdevums: Izveidot vārdnīcu, kurā atrodas atslēgas un vērtības no dict1, 
# tām atslēgām kurām vērtības ir > 500, un izvadīt jauno sarakstu.
# Piem, ja
# dict1 = {
#   1: 100,
#   2: 600,
#   3: 200,
#   4: 800
# }, tad
# dict2 = {
#   2: 600,
#   4: 800
# }
# Dots:
import random
dict1 = {}
for iii in range(0, 20):
    dict1[iii] = random.randint(0, 1000)
print(dict1)

dict2 = {}
for key, value in vardnica.items():
    if value > 500:
        dict2[key] = value
        # var lietot arī update funkciju
print(dict2)

# Uzdevums i/ni
# Cikliski izveidot vārdnīcu no sarakstiem keys un values, kur keys ir atslēgas, un values ir vērtības
# Ir garantēts, ka keys un values sarakstu garumi ir vienādi.
import random
keys = [ 1, 2, "10", 3, random.randint(10, 100) ]
values = [ "viens", 4, False, [1,3,4], random.randint(0, 100) ]
vardn = {}
for iii in range(len(keys)):
    vardn.update({keys[iii]: values[iii]})
    #vardn[iii] = values[iii]
print(vardn)
