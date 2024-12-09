a: float = float(input("Digite o primeiro lado do triângulo: "))
b: float = float(input("Digite o segundo lado do triângulo: "))
c: float = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or b == c or a == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("As medidas informadas não formam triângulo")
