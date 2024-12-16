from math import pow


def read_data():
    weight: float = float(input("Digite o peso (kg): "))
    height: float = float(input("Digite  a altura (m): "))

    return weight, height


def calc_imc(weight, height):
    return weight / pow(height, 2)


def classify_imc(imc):
    if imc < 20:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobre peso")
    else:
        print("Obeso")


weight, height = read_data()
imc = calc_imc(weight, height)
classify_imc(imc)
