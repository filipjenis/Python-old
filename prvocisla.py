#Filip Jenis, kvinta B
#Uloha: Prvocisla
num = int(input('Zadaj číslo:'))
if(num == 1):
    print('Číslo musí byť väčšie ako 1')
    
for i in range(2, num + 1):
    if(num % i == 0):
        prvocislo = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                prvocislo = 0
                break
            
        if (prvocislo == 1):
            print(i)