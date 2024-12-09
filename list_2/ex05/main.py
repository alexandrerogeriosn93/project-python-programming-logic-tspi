sum_numbers = quantity_numbers = 0

while (number := float(input("Digite um número: "))) != 0:
    sum_numbers += number
    quantity_numbers += 1

try:
    average = sum_numbers / quantity_numbers
    print(f"A média aritimética dos números é: {average:.2f}")
except ZeroDivisionError:
    print("Impossível dividir por zero.")
