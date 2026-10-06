def check_temperature(temp):
    temp_text = ""
    if temp > 25:
        temp_text = "КРИТИЧЕСКИ ЖАРКО! Включить охлаждение."
    else:
        temp_text = "Температура в норме."

    return temp_text

print("---Начало программы---")

measurements = [22, 26, 21, 28, 24]
idx = 0
for idx, measurement in enumerate(measurements, start=0):
    print(check_temperature(measurement))

print("---Конец программы---")
