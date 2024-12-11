from math import factorial

n: int = int(input("Digite o valor de N: "))

total = 0

for i in range(n + 1):
    total += factorial(i)

print(f"A soma total é: {total}")
