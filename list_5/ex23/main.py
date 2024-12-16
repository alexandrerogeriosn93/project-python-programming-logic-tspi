def read_vector(n, vet):
    for i in range(n):
        vet.append(float(input(f"Digite o {i + 1}º elemento do vetor: ")))

    return vet


def calc_positives_average(n, vet):
    sum_positives = 0
    quantity_positives = 0

    for i in range(n):
        if vet[i] > 0:
            sum_positives += vet[i]
            quantity_positives += 1

    try:
        return sum_positives / quantity_positives
    except ZeroDivisionError:
        return "Não há números positivos no vetor"


def return_quantity_negatives(n, vet):
    quantity_negatives = 0

    for i in range(n):
        if vet[i] < 0:
            quantity_negatives += 1

    return quantity_negatives


n: int = int(input("Digite a quantidade de elementos do vetor: "))
vet: list[float] = []

vet = read_vector(n, vet)
average = calc_positives_average(n, vet)
negatives = return_quantity_negatives(n, vet)

print(f"A média aritimética dos números positivos: {average}")
print(f"A quantidade de números negativos no vetor é: {negatives}")
