def read_vector(n, vet, name):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}° elemento do vetor {name}: ")))

    return vet


def calc_average(n, vet_a, vet_b, vet_c, vet_d):
    for i in range(n):
        vet_d.append((vet_a[i] + vet_b[i] + vet_c[i]) / 3)

    return vet_d


def print_vector(n, vet):
    for i in range(n):
        print(vet[i])


n: int = int(input("Digite a quantidade de elementos dos vetores A, B e C: "))
vet_a: list[float] = []
vet_b: list[float] = []
vet_c: list[float] = []
vet_d: list[float] = []

vet_a = read_vector(n, vet_a, "A")
vet_b = read_vector(n, vet_b, "B")
vet_c = read_vector(n, vet_c, "C")

vet_d = calc_average(n, vet_a, vet_b, vet_c, vet_d)

print_vector(n, vet_d)
