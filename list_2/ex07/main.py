while True:
    try:
        celsius: float = float(input("Digite a temperatura em Celsisu: "))
        fahrenheit = (9 * celsius) / 5 + 32

        print(f"{celsius}° Celsisu é equivalente a {fahrenheit:.2f} Fahrenheit.")

        option = input("Deseja repetir o processo (s/n)? ").lower()

        if option == "n":
            break
    except EOFError:
        break
