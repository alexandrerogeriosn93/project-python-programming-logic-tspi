n: int = int(input("Digite a quantidade de pessoas: "))
vet_heights: list[float] = [0 for _ in range(n)]
vet_genres: list[str] = [0 for _ in range(n)]
quantity_women = quantity_men = 0
sum_women_height = average_women_height = 0

for i in range(n):
    vet_heights[i] = float(input(f"Digite a altura da {i + 1}ª pessoa: "))
    vet_genres[i] = input(f"Digite o sexo da {i + 1}ª pessoa(m/f): ")

max_height = min_height = vet_heights[0]

for i in range(1, n):
    if vet_heights[i] > max_height:
        max_height = vet_heights[i]

for i in range(1, n):
    if vet_heights[i] < min_height:
        min_height = vet_heights[i]

for i in range(n):
    match vet_genres[i]:
        case "m":
            quantity_men += 1
        case "f":
            quantity_women += 1
            sum_women_height += vet_heights[i]

print(f"A maior altura é: {max_height}\nA menor altura é: {min_height}")

if quantity_women == 0:
    print("Não há mulheres cadastradas.")
else:
    average_women_height = sum_women_height / quantity_women
    print(f"A média da altura das mulheres é: {average_women_height}")

print(f"A quantidade de homens cadastrados é: {quantity_men}")
