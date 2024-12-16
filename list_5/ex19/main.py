from math import pow, sqrt


def read_data():
    base: float = float(input("Digite o valor da base do retângulo: "))
    height: float = float(input("Digite o valor da altura do retângulo: "))

    return base, height


def calc_diagonal(base: float, height: float) -> float:
    return sqrt(pow(base, 2) + pow(height, 2))


def calc_area(base: float, height: float) -> float:
    return base * height


def calc_perimeter(base: float, height: float) -> float:
    return base * 2 + height * 2


base, height = read_data()

diagonal = calc_diagonal(base, height)
area = calc_area(base, height)
perimeter = calc_perimeter(base, height)


print(
    f"Diagonal do retângulo? {diagonal:.2f}\nÁrea do retângulo? {area:.2f}\nPerímetro do retângulo: {perimeter:.2f}"
)
