def read_data_financing():
    property_value = float(input("Digite o valor do imóvel: "))
    entry_value = float(input("Digite o valor da entrada: "))
    installments = int(input("Digite a quantidade de prestações: "))

    return property_value, entry_value, installments


def show_installment_value(
    property_value: float, entry_value: float, installments: int
):
    try:
        installment = property_value - entry_value

        if installments > 0:
            installment /= installments

        print(f"O valor de cada prestação será: R${installment:.2f}")
    except ZeroDivisionError:
        print("Impossível dividir por zero.")


property_value, entry_value, installments = read_data_financing()
show_installment_value(property_value, entry_value, installments)
