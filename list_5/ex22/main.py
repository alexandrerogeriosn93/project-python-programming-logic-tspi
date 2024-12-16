def read_vector(n, vet):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}º elemento do vetor: ")))

    return vet


def search_value(n, vet, x):
    position = -1

    for i in range(n):
        if vet[i] == x:
            position = i
            break

    return position


n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[float] = []

vet = read_vector(n, vet)
search: float = float(input("Digite o valor a ser procurado no vetor: "))
position = search_value(n, vet, search)

if position == -1:
    print("Número não encontrado.")
else:
    print(f"Número encontrado na posição: {position}")
