with open("slowa.txt", "r") as plik:
    slowa = [i.split() for i in plik]

literaA = [i[0] for i in slowa if i[0][-1] == "A"]
literaA += [i[1] for i in slowa if i[1][-1] == "A"]

zawiera = [i[1] for i in slowa if i[0] in i[1]]

anagram = [i[1] for i in slowa if sorted(i[0]) == sorted(i[1])]

print(len(literaA), len(zawiera), len(anagram))