age: int = int(input("Digite a idade: "))

if 18 <= age < 65:
    print("maior de idade")
elif age < 18:
    print("menor de idade")
else:
    print("pessoa idosa")
