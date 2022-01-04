sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
x1 = sites['Moscow'][0]
x2 = sites['London'][0]
y1 = sites['Moscow'][1]
y2 = sites['London'][1]
res_moscow_and_london = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
x1 = sites['Moscow'][0]
x2 = sites['Paris'][0]
y1 = sites['Moscow'][1]
y2 = sites['Paris'][1]
res_moscow_and_paris = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
x1 = sites['London'][0]
x2 = sites['Paris'][0]
y1 = sites['London'][1]
y2 = sites['Paris'][1]
res_london_and_paris = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
distances = {
    "Расстояние между Московой и Лондоном" : res_moscow_and_london,
    "Расстояние между Москвой и Парижем" : res_moscow_and_paris,
    "Расстояние между Лонодоном и Парижем" : res_london_and_paris
}
print(distances)