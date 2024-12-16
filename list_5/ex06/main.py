def read_data():
    glucose: float = float(input("Digite o valor da Glicose: "))
    triglycerides: float = float(input("Digite o valor do Triglicerídios: "))
    cholesterol: float = float(input("Digite o valor do Colesterol: "))

    return glucose, triglycerides, cholesterol


def classify_glucose(glucose):
    if glucose <= 100:
        print("Normal")
    elif glucose < 140:
        print("Elevado")
    else:
        print("Diabetes")


def classify_triglycerides(triglycerides):
    if triglycerides <= 200:
        print("Desejável")
    else:
        print("Elevado")


def classify_cholesterol(cholesterol):
    if cholesterol <= 200:
        print("Desejável")
    elif cholesterol < 240:
        print("limiar")
    else:
        print("Desejável")


glucose, triglycerides, cholesterol = read_data()

classify_glucose(glucose)
classify_triglycerides(triglycerides)
classify_cholesterol(cholesterol)
