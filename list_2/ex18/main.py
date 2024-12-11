n: int = int(input("Digite o valor de N: "))

factorial = 1

for i in range(n, 0, -1):
    factorial *= i

print(f"O fatorial de {n} é: {factorial}")
