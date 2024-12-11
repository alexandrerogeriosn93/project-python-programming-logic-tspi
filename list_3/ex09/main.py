n: int = int(input("Digite a quantidade de pessoas: "))
names: list[str] = [0 for _ in range(n)]
ages: list[int] = [0 for _ in range(n)]

for i in range(n):
    names[i] = input(f"Digite o nome da {i + 1}ª pessoa: ")
    ages[i] = int(input(f"Digite a idade da {i + 1}ª pessoa: "))


max_age = ages[0]
older_person = names[0]

for i in range(1, n):
    if ages[i] > max_age:
        max_age = ages[i]
        older_person = names[i]

print(f"A pessoa mais velha é {older_person} com {max_age} anos de idade.")
