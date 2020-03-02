def ask():
    otazka = input("Cesta?").upper().split(" ")
    start = int(ord(otazka[0])-65)
    finish = int(ord(otazka[1])-65)
    if lst[(start*pocet)+finish] == 1:
        print("Cesta existuje")
    else:
        print("Cesta neexistuje")
    ask()

pocet = int(input("Pocet miest:"))
lst = []
for i in range(1, pocet+1):
    cesty = input(chr(i+64)+":").split(" ")
    for j in cesty:
        lst.append(int(j))

ask()