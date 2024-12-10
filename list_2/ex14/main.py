a: int = int(input("Digite o valor de A: "))
b: int = int(input("Digite o valor de B: "))

result = 1

for i in range(b):
    result *= a

print(f"{a} elevado a {b} é igual a: {result}")
