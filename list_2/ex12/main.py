n: int = int(input("Digite um número: "))

total = quantity = average = 0

for i in range(n):
    number: float = float(input(f"Digite o {i + 1}° número: "))
    total += number
    quantity += 1

print(f"Soma: {total}\nA média aritimética é: {total / quantity}")
