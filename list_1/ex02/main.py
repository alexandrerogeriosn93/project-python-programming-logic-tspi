base: float = float(input("Base do retângulo: "))
height: float = float(input("Altura do retângulo: "))

area = base * height
perimeter = base * 2 + height * 2

print(f"Área = {area:.4f}\nPerímetro = {perimeter:.4f}")
