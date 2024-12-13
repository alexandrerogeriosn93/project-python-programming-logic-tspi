n: int = int(input("Digite um número: "))
vet: list[float] = [0 for _ in range(n)]
total_sum = average = 0

for i in range(n):
    vet[i] = float(input(f"Digite o {i + 1}° número: "))

print("Os elementos do vetor são: ")
for i in vet:
    print(i)

for i in vet:
    total_sum += i

average = total_sum / n

print(f"Soma total: {total_sum}\nA média aritimética é: {average}")
