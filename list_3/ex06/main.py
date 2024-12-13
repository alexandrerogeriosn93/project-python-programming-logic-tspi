n: int = int(input("Digite a quantidade de elementos dos vetores: "))
vet_a: list[float] = [0 for _ in range(n)]
vet_b: list[float] = [0 for _ in range(n)]
vet_c: list[float] = [0 for _ in range(n)]

for i in range(n):
    vet_a[i] = float(input(f"Digite o {i + 1}° número do vetor A: "))

for i in range(n):
    vet_b[i] = float(input(f"Digite o {i + 1}° número do vetor B: "))

for i in range(n):
    vet_c[i] = vet_a[i] + vet_b[i]

print("Vetor C gerado:")
for i in range(n):
    print(vet_c[i])
