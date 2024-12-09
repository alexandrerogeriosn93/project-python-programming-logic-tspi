a: float = float(input("Digite o primeiro número: "))
b: float = float(input("Digite o segundo número: "))

try:
    if a % b == 0:
        print(f"{a} é divisível por {b}")
    else:
        print(f"{a} não é divisível por {b}")
except ZeroDivisionError:
    print("Impossível dividir por zero.")
