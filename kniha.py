for i in range(1,1001):
    cifsucet = sum(int(digit) for digit in str(i))
    cifsucet2 = sum(int(digit) for digit in str(i*i))
    if(cifsucet == cifsucet2):
        print(i)