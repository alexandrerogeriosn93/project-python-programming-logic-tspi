scale: str = input(
    "Deseja entrar com temperatura em Celsius ou Fahrenheit (c/f)? "
).lower()
temperature: float = float(input("Digite a temperatura: "))

match scale:
    case "f":
        celsius = (5 / 9) * (temperature - 32)
        print(f"Equivalente em Celsius: {celsius:.2f}°C")
    case "c":
        fahrenheit = (9 / 5) * temperature + 32
        print(f"Equivalente em Fahrenheit: {fahrenheit:.2f}")
    case _:
        print("Opção inválida.")
