first_number: float = float(input("Digite o primeiro número: "))
second_number: float = float(input("Digite o segundo número: "))

if first_number <= second_number:
    print(f"Números em ordem crescente: {first_number} {second_number}")
else:
    print(f"Números em ordem crescente: {second_number} {first_number}")
