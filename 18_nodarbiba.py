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
# Uzdevums: Izveidot klasi "Akcija", kas glabā informāciju par akcijām
# Nosaukums, & nominālvērtība
class Akcija:
    nosaukums :str
    nominālvērtība :float
    def __init__(self, nos, cen):
        self.nosaukums = nos
        self.nominālvērtība = cen

# Izveidot klasi AkcijuKonts, kas glabā informāciju par lietotāja naudas
# (mantot no BankasKonts) līdzekļiem un akciju līdzekļiem.
class AkcijuKonts(BankasKonts):
    akcijas: list[Akcija]
    def __init__(self):
        super().__init__()
        self.akcijas = []
    def pievienotAkc(self, akcija :Akcija):
        self.akcijas.append(akcija)
    def iznemtAkc(self, akcija :Akcija):
        self.akcijas.remove(akcija)
    def __str__(self):
        vērtība = 0.0
        output = f"Kontā ir {self.lidzekli}. Akcijas: \n"
        for akcija in self.akcijas:
            output += "* " + akcija.nosaukums + "\n"
            vērtība += akcija.nominālvērtība
        output += f"Akciju vērtība {vērtība}"
        return output
# Realizēt akciju pievienošanas un izņemšanas funkcijas.
# Izvadot objektu (print(obj)) vajadzētu izvadīt informāciju par lietotāja
# naudas atlikumu, akciju skaitu un to vērtību vērtību.
konts = AkcijuKonts()
konts.ieskaitit(100)
akc = Akcija("MSFT", 100)
konts.pievienotAkc(akc)
print(konts)

# 1. Uzd - 1. daļa
# Izveidot grafiku un klasi kas apraksta darbinieku kādā uzņēmumā. Jāuzglabā informācija par darbinieka vārdu, algu un amatu.
# Jānodefinē funkcijas - aprēķini bonusu (šai klasei funkcija atgriež vērtību 0)
# un algas aprēķins - saskaita algu + bonusa funkcijas rezultātu.
class Darbinieks:
    vards: str
    alga: float
    amats: str
    def __init__(self, vards, alga, amats):
        self.vards = vards
        self.alga = alga
        self.amats = amats
    def aprBonus(self) -> float:
        return 0.0
    def saskAlg(self) -> float:
        return self.alga + self.aprBonus()

# 2. daļa Izveidot apakšklases sekojošiem amatiem - 
# 1. Menedžeris - Glabā informāciju par to, cik darbinieki ir zem menedžera. Bonuss - darbinieku skaits * 100
# 2. Programmētājs - Glabā informāciju par to, pie kāda projekta pašlaik strādā. Bonuss  - 10% no algas
# 3. Testeris - Glabā informāciju par to, pie kāda projekta pašlaik strādā, un cik stundas ir nostrādājis šajā mēnesī. Bonuss - 5% no algas. Kopalgas aprēķinā tiek reizināta algas likme ar stundu skaitu (nevis atgriezta vienkārši alga)
class Menedzeris(Darbinieks):
    darbinieki: int
    def __init__(self, vards, alga, amats, darbinieki):
        super().__init__(vards, alga, amats)
        self.darbinieki = darbinieki
    def aprBonus(self):
        return self.darbinieki * 100
class Programmetajs(Darbinieks):
    projekts :str
    def aprBonus(self):
        return self.alga * 0.1
class Testeris(Darbinieks):
    stundas: float = 0.0
    def aprBonus(self):
        return self.alga * 0.05
    def saskAlg(self):
        return (self.alga * self.stundas) + self.aprBonus()