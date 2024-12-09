A: float = float(input("Digite o primeiro valor: "))
B: float = float(input("Digite o segundo valor: "))
C: float = float(input("Digite o terceiro valor: "))

if A > B:
    A, B = B, A
if A > C:
    A, C = C, A
if B > C:
    B, C = C, B

print(f"Valores em ordem crescente: {A} - {B} - {C}")
