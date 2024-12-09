days: int = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day: int = int(input("Digite o dia: "))
month: int = int(input("Digite o mês: "))

day_of_the_year = sum(days[: month - 1]) + day

print(f"Este é o {day_of_the_year}º dia do ano.")
