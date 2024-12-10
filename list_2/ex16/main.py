from math import pow

n: int = int(input("Digite o valor de N: "))

total = 0

for i in range(0, n + 1):
    total += pow(3, i)

print(f"A soma total da série é: {total}")
