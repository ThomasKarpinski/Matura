import statistics

with open("dane_geny.txt", "r") as plik:
    genotypy = [i.strip() for i in plik]

"""69.1-help"""
gatunki = []
for genotyp in genotypy:
    gatunki.append(len(genotyp))
gatunki = set(gatunki)
dominanta = statistics.mode(gatunki)
print(f"liczba gatunków: {len(gatunki)}\n"
      f"dominujący gatunek: {dominanta}")

"""69.2"""
licznik = 0
for genotyp in genotypy:
    if genotyp.count("BCDDC") > 1:
        licznik += 1
        continue
print(licznik)
