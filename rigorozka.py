from itertools import permutations

veta = input("Zadaj vetu:").split(" ")
moznosti = permutations(veta)

for i in moznosti: print(" ".join(i))
