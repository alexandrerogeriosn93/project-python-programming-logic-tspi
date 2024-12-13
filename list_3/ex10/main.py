n: int = int(input("Digite a quantidade de alunos: "))
names: list[str] = []
notes_first_semester: list[float] = []
notes_second_semester: list[float] = []

for i in range(n):
    names.append(input(f"Digite o nome da {i + 1}ª pessoa: "))
    notes_first_semester.append(
        float(input(f"Digite a nota do primeiro semestre da {i + 1}ª pessoa: "))
    )
    notes_second_semester.append(
        float(input(f"Digite a nota do segundo semestre da {i + 1}ª pessoa: "))
    )

print("Pessoas com notas acima da média: ")
for name, note_first, note_second in zip(
    names, notes_first_semester, notes_second_semester
):
    if (note_first + note_second) / 2 >= 6:
        print(name)
