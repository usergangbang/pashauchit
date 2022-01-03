pi_number = 3.1415926
radius = 42
point = 23, 34
square = pi_number * (radius**2)
print(f"Площадь, с точностью до 4-х знаков после запятой: {round(square, 4)}")
if point > square:
    print("Точка (23; 34) не лежит в окружности")
else:
    
