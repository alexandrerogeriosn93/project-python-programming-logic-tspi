def read_data():
    n1: float = float(input("Digite o valor de N1: "))
    n2: float = float(input("Digite o valor de N2: "))
    n3: float = float(input("Digite o valor de N3: "))
    n4: float = float(input("Digite o valor de N4: "))

    return n1, n2, n3, n4


def return_max_value(n1: float, n2: float, n3: float, n4: float) -> float:
    return max(n1, n2, n3, n4)


n1, n2, n3, n4 = read_data()
max_value = return_max_value(n1, n2, n3, n4)

print(f"O maior valor digitado é: {max_value}")
