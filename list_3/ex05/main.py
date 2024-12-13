n: int = int(input("Digite um número: "))
vet: list[int] = [0 for _ in range(n)]
quantity_even = 0

for i in range(n):
    vet[i] = int(input(f"Digite o {i + 1}° número: "))

for i in range(n):
    if vet[i] % 2 == 0:
        quantity_even += 1

if quantity_even == 0:
    print("Não foram digitados números pares.")
else:
    print("Números pares:")
    for i in range(n):
        if vet[i] % 2 == 0:
            print(vet[i])

    print(f"Quantidade de números pares: {quantity_even}")
