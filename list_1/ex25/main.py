from math import pow, sqrt

x: float = float(input("Digite o valor de x: "))

try:
    f = 5 * x + 3 / sqrt(pow(x, 2) - 16)
    print(f"f({x}) = {f}")
except ZeroDivisionError:
    print("Não definido, pois não há divisão por zero.")
except ValueError:
    print("Não definido, pois existe raiz real para números negativos.")
