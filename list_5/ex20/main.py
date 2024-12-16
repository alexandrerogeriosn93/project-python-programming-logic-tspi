def calc_value(energy: float) -> float:
    if energy <= 45:
        return 20
    else:
        return (energy - 45) * 0.5 + 20


energy: float = float(input("Digite o consumo de energia consumida: "))
total: float = calc_value(energy)

print(f"O valor total da conta de energia é: R${total:.2f}")
