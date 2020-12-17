import math

private_key=[]
public_key=[]

p=int(input("p?"))
q=int(input("q?"))

N=p*q
f=(p-1)*(q-1)

for e in range(1,f):
    if math.gcd(e,N)==1:
        if math.gcd(e,f)==1:
            private_key.append("("+str(e)+","+str(N)+")")
            for d in range(50):
                if (d*e)%f==1:
                    public_key.append("("+str(d)+","+str(N)+")")

print("Private key:")
print(" ".join(private_key))
print("Public key:")
print(" ".join(public_key))
