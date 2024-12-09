salary: float = float(input("Digite o valor do salário: "))
installment: float = float(input("Digite o valor da prestação: "))

if installment > salary * 0.30:
    print("O empréstimo não pode ser concedido.")
else:
    print("O empréstimo pode ser concedido")
