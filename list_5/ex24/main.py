def read_vectors(n, names, ages):
    for i in range(n):
        names.append(input(f"Digite o nome da {i + 1}ª pessoa: "))
        ages.append(int(input(f"Digite a idade da {i + 1}ª pessoa: ")))

    return names, ages


def return_older_person(n, names, ages):
    name_older_person = names[0]
    age_older_person = ages[0]

    for i in range(1, n):
        if ages[i] > age_older_person:
            name_older_person = names[i]
            age_older_person = ages[i]

    return name_older_person


def calc_percent_below_eighteen_years_old(n, ages):
    quantity = 0

    for i in range(n):
        if ages[i] < 18:
            quantity += 1

    try:
        return (quantity / n) * 100
    except ZeroDivisionError:
        return "Não há pessoas menores de dezoito anos de idade"


n: int = int(input("Digite a quantidade de pessoas: "))
names: list[str] = []
ages: list[int] = []

names, ages = read_vectors(n, names, ages)
older_person = return_older_person(n, names, ages)
percent = calc_percent_below_eighteen_years_old(n, ages)

print(f"A pessoa mais velha é: {older_person}")
print(f"A porcentagem de pessoas menores de dezoito anos é: {percent:.2f}%")
