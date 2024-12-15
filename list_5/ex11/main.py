def read_vector(n, vet):
    for i in range(n):
        vet.append(int(input(f"Digite o {i + 1}° elemento do vetor: ")))

    return vet


def print_even(n, vet):
    for i in range(n):
        if vet[i] % 2 == 0:
            print(vet[i])


def print_negatives(n, vet):
    for i in range(n):
        if vet[i] < 0:
            print(vet[i])


n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[int] = []

vet = read_vector(n, vet)

print("Números pares do vetor: ")
print_even(n, vet)

print("Números negativos: ")
print_negatives(n, vet)
