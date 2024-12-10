n: int = int(input("Digite o valor de N: "))

total_even = quantity_even = average = 0

for i in range(n):
    number: float = float(input(f"Digite o {i + 1}° número: "))

    if number % 2 == 0:
        total_even += number
        quantity_even += 1

try:
    average = total_even / quantity_even

    print(
        f"Soma total dos números pares: {total_even}\nA média aritimética dos números pares é: {average}"
    )
except ZeroDivisionError:
    print("Impossível dividir por zero.")
