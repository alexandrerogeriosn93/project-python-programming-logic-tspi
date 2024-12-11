n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[int] = [0 for _ in range(n)]

for i in range(n):
    vet[i] = int(input(f"Digite o {i + 1}° número do vetor: "))

percentage: float = float(input("Digite o valor da porcentagem: "))

for i in range(n):
    vet[i] += vet[i] * (percentage / 100)

print("Vetor alterado")
print(" ".join(f"{vet_final}" for vet_final in vet))
