pi_number = 3.1415926
radius = 42
point = [23, 34]
test_true = (f"True -- точка {point} лежит на окружности")
test_false = (f"False -- Точка {point} не лежит на окружности")
square = pi_number * (radius**2)
print(f"Площадь, с точностью до 4-х знаков после запятой: {round(square, 4)}")
if point[0] > radius and point[1] > radius:
    print(test_false)
elif point[0] < radius and point[1] < radius:
    print(test_true)
