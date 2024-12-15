def read_numbers():
    N1: float = float(input("Digite o valor de N1: "))
    N2: float = float(input("Digite o valor de N2: "))
    N3: float = float(input("Digite o valor de N3: "))
    N4: float = float(input("Digite o valor de N4: "))

    return N1, N2, N3, N4


def calc_average(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


n1, n2, n3, n4 = read_numbers()
average = calc_average(n1, n2, n3, n4)

print(f"A média aritimética dos números digitados é: {average:.2f}")
