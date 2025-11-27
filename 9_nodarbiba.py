saraksts = []
saraksts.append("Pievienotā vērtība")
# saraksts[10] = "123" # Nestrādās - ļauj tikai atjaunot eksistējošo indeksu

# Datu pievienošana vārdnīcai 
# Pievienošana nav - tikai atjaunošana, kas strādā kā pievienošana

# 1. var
vardnica = {}
vardnica.update({"jauna atslēga": "vērtība", "atslēga 2": "vērtība 2"})
#print(vardnica)
vardnica.update({"jauna atslēga": "jauna vērtība"})
#print(vardnica)

# 2.var 
vardnica["kaut kas"] = "2. variants pievienošanai"
#print(vardnica)

# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas 
# ir skaitļi no 1 līdz n (lietotāja ievadīts skaitlis)
# un vērtības ir šis skaitlis kvadrātā.
# piem.
# { 1: 1, 2: 4, 3: 9, 4: 16 }
n = int(input("Ievadat skaitli: "))
vardnica = {}
for iii in range(1, n+1):
    #vardnica.update({iii: iii*iii})
    vardnica[iii] = iii*iii
print(vardnica)

# Piekļūšana vērtībām
# print(vardnica.keys())
# print(vardnica.values())
# for atslēga, vērtība in vardnica.items():
#     print(f"atslēga: {atslēga}, vērtība: {vērtība}")

# Uzdevums
# Pacelt vārdnīcā "vardnica" esošās vērtības kvadrātā
for atslēga, vērtība in vardnica.items():
    vardnica[atslēga] = vērtība * vērtība
print(vardnica)

# Uzdevums:
# Ir dotas divas vārdnīcas - dict1 un dict2.
# Izveidot mainīgo dict3, kas satur dict1 un dict2 apvienojumu.
# Apvienojumu loģiku izstrādāt iekš funkcijas "apvienot_vardn"
def apvienot_vardn(dict1: 'dict[int, int]', dict2: 'dict[int, int]') -> 'dict[int, int]':
    rezultats = {}
    for atslēga, vērtība in dict1.items():
        rezultats[atslēga] = vērtība
    for atslēga, vērtība in dict2.items():
        rezultats[atslēga] = vērtība
    return rezultats

dict1 = {
    1: 10,
    2: 20,
    3: 30
}
dict2 = {
    4: 40,
    5: 50,
    6: 60
}
dict3 = apvienot_vardn(dict1, dict2)
print(dict3)

# Dzēst vērtību
#del vardnica["kaut kas"]