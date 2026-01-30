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