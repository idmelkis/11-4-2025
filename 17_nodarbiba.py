# Uzdevums:
# Izveidot grafikus un klašu definīcijas internetveikala preču grozam. Par precēm satur nosaukumu un cenu, kamēr grozs satur informāciju par precēm un to daudzumu tajā.
# Grozam jārealizē pievienošanas, izņemšanas funkcionalitāti, kā arī groza vērtības aprēķināšanu.
# Izveidot objektus grozam ar 2 precēm, aprēķināt to vērtību (preces un to vērtības var izdomāt).
class Prece:
    nosaukums :str
    cena :float
    def __init__(self, nos, cen):
        self.nosaukums = nos
        self.cena = cen
class Grozs:
    # Var būt saraksts ar vārdnīcas elementiem
    # [{'prece': Prece(), 'daudzums': 0}, ...]
    # Vai vienkārši varat pievienot vienu preci
    # vairākas reizes
    preces: list[Prece]
    
    def __init__(self):
        # Obligāti jādefinē iekš init funkc, citādi
        # vairāki grozi dalīs vienu sarakstu (!)
        self.preces = []
    def pievienotGrozam(self, prece :Prece):
        self.preces.append(prece)
    def iznemtNoGroza(self, prece :Prece):
        self.preces.remove(prece)
        # Vai:
        # for idx, prece in enumerate(self.preces): # Vēl var izmantot range...
        #     if prece.nosaukums == self.preces[idx].nosaukums:
        #         self.preces.pop(idx)
    def aprekinatCenu(self):
        total = 0.0
        for prece in self.preces:
            total += prece.cena
        return total
    
p1 = Prece("Piens", 1.25)
p2 = Prece("Maize", 1.30)
gr = Grozs()
gr.pievienotGrozam(p1)
gr.pievienotGrozam(p1)
gr.pievienotGrozam(p2)
print(f"{gr.aprekinatCenu()}€")

# Jāizveido klase "Banka Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu ja kontā ir zem €50
# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   t.i. izveidojat izņemšanas funkciju priekš krājkonta
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
# * Neļaut lietotājam izņemt naudu ja kontā ir zem €100
class BankasKonts:
    lidzekli: float
    def __init__(self):
        self.lidzekli = 0.0
    def ieskaitit(self, summa):
        self.lidzekli += summa
    def iznemt(self, summa):
        if self.lidzekli < 50.0:
            print("Nepietiek līdzekļi!")
            return
        else:
            self.lidzekli -= summa
class Krajkonts(BankasKonts):
    def iznemt(self, summa):
        if self.lidzekli < 100.0:
            print("Nepietiek līdzekļi!")
            return
        else:
            super().iznemt(summa * 1.10)
konts = Krajkonts()
konts.ieskaitit(200.0)
konts.iznemt(50)
print(konts.lidzekli)
