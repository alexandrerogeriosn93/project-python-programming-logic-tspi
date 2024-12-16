def classify_glucose(glucose):
    if glucose <= 100:
        print("Normal")
    elif glucose <= 200:
        print("Elevado")
    else:
        print("Diabetes")


glucose: int = int(input("Digite a quantidade de glicose: "))

classify_glucose(glucose)
