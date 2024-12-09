a: float = float(input("Digite o primeiro lado do triângulo: "))
b: float = float(input("Digite o segundo lado do triângulo: "))
c: float = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    print("As medidas formam triângulo.")
else:
    print("As medidas não formam triângulo.")
