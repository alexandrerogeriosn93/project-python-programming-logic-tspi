def convert_fahrenheti_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit: float = float(input("Digite a temperatura em Fahrenheit: "))
celsius = convert_fahrenheti_to_celsius(fahrenheit)

print(f"{fahrenheit} Fahrenheit é equivalente a {celsius:.2f}° Celsisu")
