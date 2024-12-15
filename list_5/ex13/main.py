from math import pow


def calc_imc(weigth, height):
    return weigth / pow(height, 2)


weight: float = float(input("Digite o peso (kg): "))
height: float = float(input("Digite a altura (m): "))

imc = calc_imc(weight, height)

print(f"O imc é: {imc:.2f}")
