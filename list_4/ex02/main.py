n: int = int(input("Digite a ordem da matriz: "))
mat = [[0 for _ in range(n)] for _ in range(n)]
vet: list[int] = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Digite o [{i}, {j}] elemento da matriz: "))

for i in range(n):
    for j in range(n):
        vet[i] += mat[i][j]

print("Vetor gerado")
print(*vet)
