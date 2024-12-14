lines: int = int(input("Digite a quantidade de linahs da matriz: "))
columns: int = int(input("Digite a quantidade de colunas da matriz: "))
mat = [[0 for _ in range(columns)] for _ in range(lines)]

for i in range(lines):
    for j in range(columns):
        mat[i][j] = float(input(f"Digite o elemento [{i}, {j}] da matriz: "))

print("Matriz gerada")
for i in range(lines):
    print(" ".join(map(str, mat[i])))
