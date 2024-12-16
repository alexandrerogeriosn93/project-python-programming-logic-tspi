def read_vector(n, vet):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}º elemento do vetor: ")))

    return vet


def sum_vector(n, vet):
    total = 0

    for i in range(n):
        total += vet[i]

    return total


def average_vector(n, vet):
    return sum_vector(n, vet) / len(vet)


def max_position_index(n, vet):
    max_value = vet[0]
    position = 0

    for i in range(1, n):
        if vet[i] > max_value:
            max_value = vet[i]
            position = i

    return position


n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[float] = []

vet = read_vector(n, vet)

sum_total = sum_vector(n, vet)
average = average_vector(n, vet)
position = max_position_index(n, vet)

print(f"A soma de todos os elementos do vetor é: {sum_total}")
print(f"A média aritimética dos elementos do vetor é: {average}")
print(f"A posição do maior elemento do vetor é: {position}")
