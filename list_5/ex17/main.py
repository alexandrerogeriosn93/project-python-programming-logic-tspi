def validate_grade(note, note_id):
    while (
        note := float(input(f"Digite o valor da nota {note_id}: "))
    ) < 0 or note > 25:
        print("Nota inválida")

    return note


def read_data(n1, n2, n3):
    n1 = validate_grade(n1, "A")
    n2 = validate_grade(n2, "B")
    n3 = validate_grade(n3, "C")

    return n1, n2, n3


def sum_grades(n1, n2, n3):
    return n1 + n2 + (n3 * 2)


def show_message(grade):
    if grade >= 70:
        print("Aprovado")
    else:
        print("Reprovado")


n1 = n2 = n3 = 0

n1, n2, n3 = read_data(n1, n2, n3)
final_grade = sum_grades(n1, n2, n3)

print(f"Nota final: {final_grade}")
show_message(final_grade)
