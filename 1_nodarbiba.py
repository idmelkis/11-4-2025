# KOMENTĀRS
# Palaist programmu - f5 poga!!! 
# (pirmajā reizē - bultiņa uz leju (iezīmējam Python debugger) - Enter - Enter)
# Regulāri spiežam ctrl+s
print("Sveika izvade") # print("Sveika izvade")
# Automātiska komentēšana: Ctrl + /
"""
 Vairāku
 Rindu
 Komentārs
"""

teksts = "vērtība"
skaitļi = 1
daļskaitļi = 1.0
būla = True # vai False - patiess vai nepatiess
saraksts = [ 123, "teksts", True ]

rezultāts = "1" + str(1)
print(rezultāts)

rezultāts = int("1") + 1
#rezultāts = float("1") + 1
print(rezultāts)
#mainīgais = skaitļi

# Izvade
#print("Teksts: " + str(rezultāts)) # Neiesaku
print("Teksts: ",rezultāts,"!")
print(f"Teksts: {rezultāts}!")
# Izvade vairākās rindās
print("""Vairāku
Rindu
izvade
""") 
print("Vairāku\nrindu\nizvade")
print(r"Vairāku\nrindu\nizvade")

mainīgais = "Vairāku\nrindu\nizvade"
print(mainīgais)
print(f"Garums: {len(mainīgais)}")
print(mainīgais[2]) #
# saraksts = [ 123, "teksts", True ]
# print(saraksts[0])

#print(len(saraksts))
teksts = "123"
saraksts = ["1","2","3"]
print(len(teksts))
print(len(saraksts))
# mainīgais[<sākums>:<beigas>]
print(mainīgais[2:3])
print(saraksts[1:2])

# Uzdevums: Ir dots skaitlis 1234 mainīgajā. Izvadam trešo ciparu (3).
skaitlis = 1234
print(str(skaitlis)[2])

# Nākošajā stundā: If/else