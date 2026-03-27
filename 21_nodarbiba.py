import os
os.chdir(os.path.dirname(__file__))

# Atvērt failu
# Neiesaku lietot - manuāli jāaizver fails
#mainīgais = open()
#mainīgais.close()

# Open parametri:
# 1. Faila nosaukums
# 2. Faila atvēršanas režīms
# read - r - lasīt failu
# write - w - rakstīt failā - ja fails neeksistē to izveido, ja fails eksistē - to pārraksta
# append - a - raksta failā - fails tiek izveidots ja tas neeksistē, ja eksistē - tam pievieno datus
# read + append - r+ - atver failu režīmā, kurā varat gan lasīt, gan pievienot datus failam
# write + read - w+ - atver failu režīmā, kurā varat gan lasīt, gan rakstīt failā - fails tiks izveidots pa jaunu, kad to atvērsiet
# Vairāk informācija: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Binārā faila atvēršana - pievieno burtu b, piem. "wb"
# 3. Kodējums - vienmēr UTF-8
# with open(".\\fails.ignored", "r", encoding="UTF-8") as faila_mainīgais: # N.B. faila mainīgā nosaukums var būt jebkāds
#     print("Fails atvērts")
    #faila_mainīgais.write("Teksts kuru rakstīt!\n") # \n - jauna rinda
    #faila_mainīgais.writelines(["Pirmā rinda\n", "Otrā rinda\n", "Trešā rinda\n"]) # Lai gan nosaukums ir writelines, \n tik un tā ir jāpievieno katram saraksta elementam. Lieto lai ierakstītu saraksta elementus failā.
    
    # Ja jums ir saraksts, kuram elementiem nav \n simboli -
    # saraksts = ["Pirmā rinda", "Otrā rinda", "Trešā rinda"]
    # for line in saraksts:
    #     faila_mainīgais.write(line + "\n")
    # dati = ""
    # for line in faila_mainīgais:
    #     #print(line, end="") # Noņem jaunas rindas simbolu no print() komandas izvades
    #     #print(line.strip()) # Noņem jaunas rindas simbolu no rindas, kas ir nolasīta no faila
    #     dati += line
    # print(dati)
    # print(dati[:4]) # Pirm
    
    # # Tiešā lasīšana no faila - Kursors iet uz priekšu par noteiktu simbolu skaitu
    # print(faila_mainīgais.read(3)) # Pirmie trīs burti - Pir
    # print(faila_mainīgais.read(3)) # Nākošie trīs burti - "mā "
    # print(faila_mainīgais.read(3)) # Nākošie trīs burti - rin
    
    # # Pārvieto kursoru uz faila sākumu
    # faila_mainīgais.seek(0,0)
    # print(faila_mainīgais.read(3)) # Pirmie trīs burti - Pir
    # print(faila_mainīgais.read(3)) # Nākošie trīs burti - "mā "
    # Pārvietot kursoru uz trešo baitu
    #faila_mainīgais.seek(3,0)
    #print(faila_mainīgais.read(3)) #"mā "
    # Ja pievieno failam sākumā emoji, piem 👍
    # faila_mainīgais.seek(3,0)
    # Tad
    #print(faila_mainīgais.read(3))
    # Izvadīs kļūdu, jo emoji ir 4 baitus liels - būs kļūda.
    # Lietojot
    #faila_mainīgais.seek(4,0)
    # print(faila_mainīgais.read(3))
    # Izvadīs "Pir", kas ir pirmie 3 burti pēc šī emoji
    #faila_mainīgais.seek(0,0)
    #print(faila_mainīgais.read(13)) # Izvada: Pirmā rinda\nO
#print("Fails aizvērts") 

# Uzdevums: 
# Pitonā ar open funkciju izveidot failu, pieprasīt no lietotāja kādu ievadi, un ierakstat to [ievadi] failā
with open(".\\fails.ignored", "w", encoding="UTF-8") as f:
    f.write(input()+"\n")

# Nākošajā stundā: Uzdevumi, json/csv, mapju pārvalde