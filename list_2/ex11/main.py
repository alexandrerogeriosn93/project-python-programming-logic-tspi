x: int = int(input("Digite o primeiro número: "))
n: int = int(input("Digite o segundo número: "))

for i in range(n + 1):
    print(f"{x} x {i} = {x * i}")
