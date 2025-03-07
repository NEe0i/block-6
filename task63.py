grades = []


print("Введите 28 оценок по информатике (от 2 до 5) для учеников класса:")
for i in range(28):
    while True:
        try:
            grade = int(input(f"Оценка для ученика {i + 1}: "))
            if grade in (2, 3, 4, 5):
                grades.append(grade)
                break
            else:
                print("Пожалуйста, введите оценку от 2 до 5.")
        except ValueError:
            print("Пожалуйста, введите целое число.")


if 2 in grades:
    print(" оценках есть двойки.")
else:
    print(" оценках нет двойки.")