x: float = float(input("Digite o valor desejado: "))
a: float = float(input("Digite o primeiro valor do intervalo: "))
b: float = float(input("Digite o segundo valor do intervalo:"))

if a > b:
    a, b = b, a

if a <= x <= b:
    print(f"{x} está no intervalo fechado [{a},{b}]")
else:
    print(f"{x} não está no intervalo [{a},{b}]")
