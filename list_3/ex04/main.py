n: int = int(input("Digite um número: "))
vet: list[float] = [0 for _ in range(n)]

for i in range(n):
    vet[i] = float(input(f"Digite o {i + 1}° número: "))

position = 0
max_value = vet[0]

for i in range(1, n):
    if vet[i] > max_value:
        max_value = vet[i]
        position = i

print(f"A posição do maior valor no vetor é: {position}")
