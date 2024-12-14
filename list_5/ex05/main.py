def print_multiplication_table(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


n: int = int(input("Digite um número para mostrar a sua tabuada: "))

print_multiplication_table(n)
