# Klase - abstrakcija objektiem
class Nosaukums:
    pass
#nosaukums = [Nosaukums, Nosaukums]

class Filma:
    nosaukums: str
    zanrs: str
class Kinoteatris:
    # Mainīgo definīcijas - var nepiešķirt standarta vērtības
    _irAtverts :bool
    nosaukums :str
    filmas :list[Filma] = []

    # Python iebūvētās klašu funkcijas

    # Tiek palaista katru reizi, kad izveido objektu
    def __init__(self, nosaukums):
        # print("Tiek palaista katru reizi, kad izveido objektu")
        self.nosaukums = nosaukums
        print(f"Izveidots kinoteātis {nosaukums}")
        # Standarta vērtību piešķiršana (ja tas nav izdarīts tieši zem klases definīcijas)
        #self.filmas = []
        self._irAtverts = False

    # Tiek palaista katru reizi, kad objektu pārveido
    # par tekstu, piem. iekš print()
    def __str__(self):
        return f"Nosaukums: {self.nosaukums}, Filmas: {self.filmas}, Atvērts: {self._irAtverts}"
    
    # Vienkāršas - mūsu definētas funkcijas
    def atvertKinoteatri(self):
        self._irAtverts = True
    def aizvertKinoTeatri(self):
        self._irAtverts = False
    def pievienotFilmu(self, filma :Filma):
        self.filmas.append(filma)
    
    # Getter/Setter funkcijas
    def getNosaukums(self) -> str:
        return self.nosaukums
    def setNosaukums(self, nosaukums):
        if nosaukums == "": # Izmet kļūdu, ja tukšs
            raise Exception("Nosaukums nevar būt tukšs")
        self.nosaukums = nosaukums
 

mainigais = Filma() # šis mainīgais ir objekts

kinoteatris = Kinoteatris("Kino 1")
print(kinoteatris)
kinoteatris.atvertKinoteatri()
print(kinoteatris)
#kinoteatris.setNosaukums("")
kinoteatris.aizvertKinoTeatri()
print(kinoteatris)

# Izvada visus mainīgos objektā kā vārdnīcu - var noderēt atkļūdošanai
print(kinoteatris.__dict__)
# kinoteatris_1 = Kinoteatris("Kino 2")
# print(kinoteatris_1)
# kinoteatris_2 = Kinoteatris("Kino 3")
# print(kinoteatris_2)

class Profils:
    # 1. solis - mainīgie
    aktivs = True
    lietotajvards :str
    vards :str
    uzvards :str
    ieraksti :list = []

    # 2. solis - init funkcija
    def __init__(self, lietotajvards, vards, uzvards):
        self.lietotajvards = lietotajvards
        self.vards = vards
        self.uzvards = uzvards
    
    # 3. solis - mūsu pašu funkcijas
    def izveidot_ierakstu(self,ieraksts :str):
        self.ieraksti.append(ieraksts)
    def izdzest_kontu(self):
        self.aktivs = False
    def izmainit_konta_informaciju(self, lietotajvards, vards, uzvards):
        self.lietotajvards = lietotajvards
        self.vards = vards
        self.uzvards = uzvards
    def tuksa_funkcija():
        pass

# Praktiska pielietošana
janis = Profils("janisb", "Jānis", "Bērziņš")
peteris = Profils("xXpeteris1337Xx", "Pēteris", "Egle")
print(janis.__dict__)
print(peteris.__dict__)

# Uzdevums - skat 14_nodarbiba.drawio failu
class Prieksmets:
    nosaukums :str
    skolotajaVards :str
    skolenuSkaits :int = 0
    skoleni :list[str] = []
    nodarbibuDatumi :list[str] = []

    def __init__(self, nosaukums, skolotajaVards):
        self.nosaukums = nosaukums
        self.skolotajaVards = skolotajaVards
    
    def izveidotNodarbibu(self, datums):
        self.nodarbibuDatumi.append(datums)
    def pievienotSkolenu(self, skolenaVards):
        self.skoleni.append(skolenaVards)
        self.skolenuSkaits = len(self.skoleni)
    def izvaditSkolenus(self):
        print(self.skoleni)
    
    def __str__(self):
        return f"Priekšmets {self.nosaukums} kurā mācās {self.skolenuSkaits} skolēni"
    
programmesana = Prieksmets("Programmēšana I", "Ingmārs")
programmesana.pievienotSkolenu("Anna")
print(programmesana.izvaditSkolenus())
print(programmesana)