from math import sqrt

L1: float = float(input("Digite o primeiro lado do triângulo: "))
L2: float = float(input("Digite o segundo lado do triângulo: "))
L3: float = float(input("Digite o terceiro lado do triângulo: "))

if not L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print("As medidas não formam triângulo.")
else:
    T = (L1 + L2 + L3) / 2
    area = sqrt(T * (T - L1) * (T - L2) * (T - L3))

    print(f"A área do triângulo é {area:.2f}")
