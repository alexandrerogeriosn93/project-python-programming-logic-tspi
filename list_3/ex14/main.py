children: int = int(input("Digite a quantidade de crianças nascidas: "))
genres: list[str] = []
ages: list[int] = []
children_dead = 0
children_male_dead = 0
children_below_twenty_four_months_dead = 0

while (gender := input("Digite o sexo da criança: ")) != "vazio":
    genres.append(gender)
    ages.append(int(input("Digite os meses de vida da criança: ")))
    children_dead += 1

for gender, age in zip(genres, ages):
    if gender == "masculino":
        children_male_dead += 1

    if age <= 24:
        children_below_twenty_four_months_dead += 1


percent_children_dead = (children_dead / children) * 100
percent_children_male_dead = (children_male_dead / children) * 100
percent_children_below_twenty_four_months_dead = (
    children_below_twenty_four_months_dead / children
) * 100

print(f"A porcentagem de crianças mortas no período: {percent_children_dead:.2f}%")
print(
    f"A porcentagem de crianças do sexo masculino mortas no período: {percent_children_male_dead:.2f}%"
)
print(
    f"A porcentagem de crianças que viveram 24 meses ou menos no período: {percent_children_below_twenty_four_months_dead:.2f}"
)
