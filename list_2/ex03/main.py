from math import pow

a = float(input("Digite o valor de A: "))

while (b := float(input("Digite o valor de B: "))) < 0:
    pass

print(f"{a} elevado a {b} é igual a {pow(a, b)}")
