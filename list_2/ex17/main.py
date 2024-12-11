from math import pow

x: int = int(input("Digite o valor de X: "))
n: int = int(input("Digite o valor de N: "))

total = 0

for i in range(1, n + 1):
    total += pow(x, i * 2)
    # print(f"{x} ^ {i * 2} = {pow(x, i * 2)}\nTotal: {total}")


print(f"A soma total da série é: {total}")
