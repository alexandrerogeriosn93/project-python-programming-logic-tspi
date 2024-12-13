n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[float] = [0 for _ in range(n)]

total_sum = average = 0
under_average = False

for i in range(n):
    vet[i] = float(input(f"Digite o {i + 1}° elemento do vetor: "))

for i in range(n):
    total_sum += vet[i]

average = total_sum / n

print(f"A média aritimética dos elementos do vetor é: {average}")

for i in range(n):
    if vet[i] < average:
        under_average = True
        break

if not under_average:
    print("Não há elementos abaixo da média")
else:
    print("Números abaixo da média")
    for i in range(n):
        if vet[i] < average:
            print(vet[i])
