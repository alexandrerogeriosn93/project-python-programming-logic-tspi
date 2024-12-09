from math import pow, sqrt

cathetus_a: float = float(input("Digite o valor do cateto oposto: "))
cathetus_b: float = float(input("Digite o valor do cateto adjacente: "))

hypotenuse = sqrt(pow(cathetus_a, 2) + pow(cathetus_b, 2))
perimeter = cathetus_a + cathetus_b + hypotenuse
area = (cathetus_a * cathetus_b) / 2

print(f"Hipotenusa: {hypotenuse}\nPerímetro: {perimeter}\nÁrea: {area}")
