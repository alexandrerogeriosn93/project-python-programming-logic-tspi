def convert_real_to_dollar(real, exchange_rate):
    try:
        return real / exchange_rate
    except ZeroDivisionError:
        return "Impossível dividir por zero."


dollar: float = float(input("Digite o valor do Dóllar: "))
real: float = float(input("Digite a quantidade de Reais: "))

quantity_dollars = convert_real_to_dollar(real, dollar)

print(
    f"A quantidade de Dóllares que pode comprar com R${real:.2f} é: ${quantity_dollars:.2f}"
)
