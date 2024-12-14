m = int(input("Quantas linhas vai ter cada matriz? "))
n = int(input("Quantas colunas vai ter cada matriz? "))

mat_a = [[0 for _ in range(n)] for _ in range(m)]
mat_b = [[0 for _ in range(n)] for _ in range(m)]
mat_c = [[0 for _ in range(n)] for _ in range(m)]

print("\nPrimeira matriz:")
for i in range(m):
    for j in range(n):
        mat_a[i][j] = int(input(f"Elemento [{i + 1}, {j + 1}]: "))

print("\nSegunda matriz:")
for i in range(m):
    for j in range(n):
        mat_b[i][j] = int(input(f"Elemento [{i + 1},{j + 1}]: "))

for i in range(m):
    for j in range(n):
        mat_c[i][j] = mat_a[i][j] + mat_b[i][j]

print("\nMatriz gerada:")
for i in range(m):
    for j in range(n):
        print(f"{mat_c[i][j]} ", end="")
    print()
