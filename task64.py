powers = list(map(int, input("Введите 30 значений мощности пробел: ").split()))
found = False

for i, power in enumerate(powers):
    if power > 200:
        print(f"Первая модель  мощ более 200 находится {i + 1} c {power}")
        found = True
        break

if not found:
    print("Нет авто  мощностью более 200 л ")