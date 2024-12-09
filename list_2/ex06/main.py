max_value = 0

while (number := float(input("Digite um número: "))) != 0:
    if number > max_value:
        max_value = number

print(f"O maior valor digitado é {max_value}")
