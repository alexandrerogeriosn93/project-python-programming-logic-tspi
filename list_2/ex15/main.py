n: int = int(input("Digite o valor de N: "))

total = 0

for i in range(1, n + 1):
    total += 1 / (2 * i)

print(f"O valor total da soma {total:.4f}")
