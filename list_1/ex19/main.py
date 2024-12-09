a: float = float(input("Digite o primeiro número: "))
b: float = float(input("Digite o segundo número: "))

if a == b:
    print("Os números são iguais.")
elif a < b:
    print(f"{a} é o menor número e {b} é o maior número.")
else:
    print(f"{b} é o menor número e {a} é o maior número.")
