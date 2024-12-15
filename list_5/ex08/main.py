def read_vector(n, vet):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}° elemento do vetor: ")))

    return vet


def print_positives(n, vet):
    for i in range(n):
        if vet[i] > 0:
            print(vet[i])


n: int = int(input("Digite a quantidade de números do vetor: "))
vet: list[float] = []

vet = read_vector(n, vet)
print_positives(n, vet)
