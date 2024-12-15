def read_data(n, vet_names, vet_ages):
    for i in range(n):
        vet_names.append(input(f"Digite o nome da {i + 1}ª pessoa: "))
        vet_ages.append(int(input(f"Digite a idade da {i + 1}ª pessoa: ")))

    return vet_names, vet_ages


def print_people_with_age_between_twelve_and_twenty_years(vet_names, vet_ages):
    for name, age in zip(vet_names, vet_ages):
        if 12 <= age <= 20:
            print(name)


n: int = int(input("Digite a quantidade de pessoas: "))
vet_names: list[str] = []
vet_ages: list[int] = []

vet_names, vet_ages = read_data(n, vet_names, vet_ages)

print("Pessoas com idades entre 12 e 20 anos:")
print_people_with_age_between_twelve_and_twenty_years(vet_names, vet_ages)
