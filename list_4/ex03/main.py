n: int = int(input("Digite a ordem da matriz: "))
mat = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = float(input(f"Digite o elemento [{i + 1}, {j + 1}] da matriz: "))

sum_positives = sum(
    map(lambda x: x if x > 0 else 0, [element for i in mat for element in i])
)

print(f"\nA soma dos números positivos é: {sum_positives:.1f}")

row_index: int = int(input("\nDigite o índice da linha: "))
print(f"Elementos da {row_index}ª linha: ", end="")
print(*map(lambda x: x, mat[row_index - 1]))

column_index: int = int(input("\nDigite o índica da coluna: "))
print(f"Elementos da {column_index}ª coluna: ", end="")
print(*map(lambda row: row[column_index - 1], mat))

print("\nDiagonal principal: ", end="")
print(*map(lambda i: mat[i][i], range(len(mat))))

mat_updated = [
    [(lambda x: x**2 if x < 0 else x)(mat[i][j]) for j in range(n)] for i in range(n)
]

print("\nMatriz alterada:")
for row in mat_updated:
    print(*row)
