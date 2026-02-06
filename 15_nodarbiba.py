# Uzdevums: Izveidot klašu diagrammu automašīnai.
# Jārealizē automašīnas braukšanas stāvoklis (ieslēgts, ātrums),
# kā arī paātrinājuma un bremzēšanas funkcionalitāte.
#
# Pēc tam - izveidot klases definīciju
class Automašīna:
    ieslegts :bool = False
    atrums: float = 0.0
    marka: str
    modelis: str
    def __init__(self, marka, modelis):
        self.marka = marka
        self.modelis = modelis  
    def ieslegtMasinu(self):
        if not self.ieslegts:
            self.ieslegts = True
        else:
            print("Masina jau ir ieslegta")
    def izslegtMasinu(self):
        if self.ieslegts:
            self.ieslegts = False
        else:
            print("Masina jau ir izslegta")
    def paatrinat(self, atrums :float):
        self.atrums += atrums
    def bremzet(self, atrums :float):
        self.atrums -= atrums
# Pielietošana:
masina_1 = Automašīna("Toyota", "Corolla")
masina_1.ieslegtMasinu()
masina_1.paatrinat()
# ...


#Uzdevums: Izveidot klašu diagrammu un klases definīciju bezvadu austiņām. 
#Klasei jābūt identificējošai informācijai (modelis, brends utt.), savienošanās stāvoklis, skaļuma līmenis. Jārealizē pievienošanās, atslēgšanās, skaņas līmeņa izmaiņas un dziesmas spēlēšanas funkcionalitāte
#Izveidot objektu - palaist savienošanās, savienošanās, skaņas līmeņa palielināšanas un dziesmas spēlēšanas funkcijas.
# (!) Klasei jāatbilst diagrammai 1:1
# Jāiesniedz gan .drawio, gan .py fails.
class Austinas:
    modelis :str
    brends :str
    savienots :bool = False
    skalums :float = 0.0
    dziesmas_statuss :str = ""

    def __init__(self, modelis, skalums):
        self.modelis = modelis
        self.skalums = skalums
    def pieslegties(self):
        # Uzlabot: sekot kādai ierīcei ir pieslēdzies
        self.savienots = True
    def atslegties(self):
        # Uzlabot: sekot kādai ierīcei ir pieslēdzies
        self.savienots = False
    def palielinat_skalumu(self):
        # Var padot arī kā parametru - vai vienkārši palielināt par noteiktu %
        self.skalums += 5
    def samazinat_skalumu(self):
        if self.skalums > 0: # Skaļums nevar būt negatīvs!
            self.skalums -= 5
    def spelet_dziesmu(self, dziesma):
        # Uzlabot: sekot līdzi dziesmas statusam
        print(f"Spēlē {dziesma}")
        self.dziesmas_statuss = dziesma
    def __str__(self):
        return f"{self.brends} {self.modelis} - Skaļums {self.skalums} - {self.dziesmas_statuss if len(self.dziesmas_statuss) > 0 else ''}"


#Izveidot objektu - palaist savienošanās, skaņas līmeņa palielināšanas un dziesmas spēlēšanas funkcijas, jāizvada informācija par austiņām (__str__).
obj = Austinas("???", "???")
obj.savienots()
obj.palielinat_skalumu()
print(obj)