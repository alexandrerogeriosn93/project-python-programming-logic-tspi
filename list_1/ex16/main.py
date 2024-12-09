from math import pow, sqrt

number: float = float(input("Digite um número: "))

if number >= 0:
    print(f"A raiz quadrade do número {number} é: {sqrt(number)}")
else:
    print(f"O número {number} elevado ao quadrado é: {pow(number, 2)}")
