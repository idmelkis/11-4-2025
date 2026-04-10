# Uzdevums: 
# Pitonā ar open funkciju izveidot failu ar sekojošu saturu:
# 123
# 234
# 456
with open(".\\fails.ignored", "w", encoding="UTF-8") as f:
    f.write("123\n234\n456\n999")
# Uzdevums: Atverat šo failu iekš python; saskaitat failā
# esošos skaitļus un izvadat rezultātu.
# with open(".\\fails.ignored", "r", encoding="UTF-8") as f:
#     summa = 0
#     for line in f:
#         summa += int(line)
#     print(summa)
# Uzdevums: atverat šo pašu failu iekš python, iekš Python
# izveidojat jaunu failu "kopija", un saglabājat šī faila saturu
# tajā.
with open(".\\fails.ignored", "r", encoding="UTF-8") as f:
    with open(".\\kopija.ignored", "w", encoding="UTF-8") as f2:
        for line in f:
            f2.write(line)
# Uzdevums: Iekš Python, izveidojat failu ar nosaukumu "tagad", 
# kas katru reizi, kad palaižat programmu pievieno pašreizējo 
# laiku faila beigās. Izmantojat doto datetime funkciju!
import datetime
#print(datetime.datetime.now())
with open(".\\tagad.ignored", "a", encoding="UTF-8") as fails:
    fails.write(str(datetime.datetime.now())+ "\n")

# JSON - JavaScript Object Notation
# Veids kā attēlot strukturētus datus teksta formātā
vārdnīca = {
    'atslēga': 'vērtība',
    "True": False,
    "skaitlis": 123
}
print(vārdnīca["atslēga"])

import json
# 1. Pārveidot vārdnīcu tekstā
# dumps- dump string. Lai pieslēgtu garumzīmes - ensure_ascii jauzliek false
print(json.dumps(vārdnīca, ensure_ascii=False))
# 2. Pārveidot tekstu par vārdnīcu
json_str = '{"atsl": "vērt", "bool": true}'
# loads - load string
vārdnīca = json.loads(json_str)
print(vārdnīca)
print(vārdnīca["bool"])

# Uzdevums: Dota sekojošā vārdnīca
lietotajs = {
    "lietotājvārds": "",
    "parole": ""
}
# Programmai jāiegūst ievade no lietotāja - lietotājvārds un parole (input)
# Un jāsaglabā šīs vērtības vārdnīcā. Šī vārdīca jāsaglabā failā kā json ar nosaukumu
# lietotajs.json
lietotajs["lietotājvārds"] = input()
lietotajs["parole"] = input()
with open(".\\lietotajs.json", "w", encoding="UTF-8") as fails:
    f.write(json.dumps(lietotajs, ensure_ascii=False))

# Nākošajā stundā - csv, i/ni