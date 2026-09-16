print("---Начало программы---")

grades = [5, 3, 4, 2, 5, 4, 3, 2]
idx = 0
for idx, grade in enumerate(grades, start=0):
    if grade == 2:
        print("Оценка 2 — нужно пересдать!")
    else:
        print(f"Оценка {grade} — хорошая работа!")

print("---Конец программы---")