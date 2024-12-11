n: int = int(input("Digite o valor de N: "))
vet: list[int] = [0 for _ in range(n)]
odd = False

for i in range(n):
    number = int(input(f"Digite o {i + 1}° número: "))
    vet[i] = number

    if number < 0:
        odd = True

if not odd:
    print("Não há números negativos no vetor.")
else:
    print("Os número negativos são:")
    for i in vet:
        if i < 0:
            print(i)
