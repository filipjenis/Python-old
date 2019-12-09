pismeno = input("Zadaj písmeno na nahradenie samohlások:")
veta = input("Zadaj vetu:")
veta_upravena = ""

for i in veta:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        i = pismeno
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        i = pismeno.upper()
    veta_upravena += i
print(veta_upravena)