n: int = int(input("Digite o valor de N: "))
vet: list[float] = [0 for _ in range(n)]

for i in range(n):
    vet[i] = float(input(f"Digite o {i + 1}° número: "))

max_value = vet[0]

for i in range(1, n):
    if vet[i] > max_value:
        max_value = vet[i]

print(f"O maior valor digitado é {max_value}")
