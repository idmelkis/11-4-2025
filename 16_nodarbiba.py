# Saistītas klases
# 1. Klase ar klases mainīgo
# Piemērs:
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.
class Spuldze:
    brends :str
    modelis :str
    krāsa :str # vai krāsas temperatūra
    ieslēgts :bool
    def __init__(self):
        # TODO: init parametri
        pass
    def ieslegt(self):
        self.ieslēgts = True
    def izslegt(self):
        self.ieslēgts = False
# Idejiski lampas klase kontrolē spuldzi - spuldzi pašu izmainīt nedrīkstētu
class Lampa:
    brends :str
    modelis :str
    izmērs :str
    krāsa :str
    spuldze :Spuldze
    def __init__(self):
        # TODO: init parametri
        self.spuldze = Spuldze()
    def ieslegt_spuldzi(self):
        self.spuldze.ieslegt()
    # TODO: izslēgt

# 2. Mantošana
# Transportlīdzekļi => Automašīna, Autobuss, Vilciens...
class Transportlīdzeklis:
    brends :str
    modelis :str
    ātrums :float = 0.0
    riteņu_skaits: int = 0
    durvju_skaits: int = 0
    def __init__(self, brends, modelis):
        self.brends = brends
        self.modelis = modelis
    def paatrināt(self, ātrums):
        self.ātrums += ātrums
# apakšklasi norādam iekavās (var būt vairākas - atdala ar komatu)
class Automašīna(Transportlīdzeklis):
    def __init__(self, brends, modelis):
        self.riteņu_skaits = 4
        self.durvju_skaits = 4
        # super ļauj piekļū virsklases mainīgajiem un funkcijām
        # super ieteicams izmantot tikai lai izsauktu virsklases funkcijas
        # mainīgie - tikai ar self.<main>.
        super().__init__(brends, modelis)
class Lidmašīna(Transportlīdzeklis):
    spārnu_platums :float
    def __init__(self, brends, modelis):
        self.spārnu_platums = 10.0
        super().__init__(brends, modelis)
obj = Automašīna("", "")
print(obj.riteņu_skaits)
obj.paatrināt(10) # virsklases funkcija
print(obj.ātrums) # virsklases mainīgais
obj2 = Lidmašīna("", "")
obj2.spārnu_platums # nav pieejams automašīnai

#Uzdevums:
#* Izveidot grafiku un klasi "dzīvnieks". Parametrs - vārds, kāju skaits. Funkcija - skaņa (neko neizvada).
#* Izveidot grafiku un apakšklasi "suns". Funkcija skaņa (izvada "Rej").
#* Izveidot grafiku un apakšklasi "kaķis". Funkcija skaņa (izvada "Ņaud")
class Dzīvnieks:
    vārds :str
    kāju_skaits :int = 0
    def __init__(self, vārds):
        self.vārds = vārds
    def skaņa(self):
        print("Palaista skaņa() funkcija virsklasē")
        return None
class Suns(Dzīvnieks):
    astes_garums :float
    def __init__(self, vārds):
        self.kāju_skaits = 4
        super().__init__(vārds)
    def skaņa(self):
        #super().skaņa()
        return "Rej"
class Kaķis(Dzīvnieks):
    astes_garums :float
    def __init__(self, vārds):
        self.kāju_skaits = 4
        super().__init__(vārds)
    def skaņa(self):
        return "Ņaud"
suns = Suns("AAA")
kaķis = Kaķis("BBB")
print(f"Suns {suns.skaņa()}, kaķis {kaķis.skaņa()}")