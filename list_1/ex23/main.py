from math import pow

weight: float = float(input("Digite o peso (em kg): "))
height: float = float(input("Digite a altura (em m): "))

imc = weight / (pow(height, 2))

if imc < 20:
    print(f"Imc: {imc:.2f} abaixo do peso")
elif imc < 25:
    print(f"Imc: {imc:.2f} peso normal")
elif imc < 30:
    print(f"Imc: {imc:.2f} sobre peso")
else:
    print(f"Imc: {imc:.2f} obeso")
