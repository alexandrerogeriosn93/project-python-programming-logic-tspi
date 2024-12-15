def read_vector(n, vet):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}° elemento do vetor: ")))

    return vet


def sum_value(n, vet, x):
    for i in range(n):
        vet[i] += x

    return vet


def print_vector(n, vet):
    for i in range(n):
        print(vet[i])


n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[float] = []

vet = read_vector(n, vet)

x: float = float(input("Digite o valor para ser somado a cada elemento do vetor: "))
vet = sum_value(n, vet, x)

print_vector(n, vet)
