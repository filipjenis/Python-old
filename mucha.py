#Filip Jenis, kvinta B
#Úloha: Sedí mucha na stene
pismeno = input("Zadaj písmeno na nahradenie samohlások:")
veta = input("Zadaj vetu:")
veta_upravena = ""

for i in veta:
    if i.isupper():
        velke_pismeno = 1
    else:
        velke_pismeno = 0
    i = i.lower()
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        i = pismeno
    if velke_pismeno == 1:
        i = i.upper()
    veta_upravena += i
print(veta_upravena)