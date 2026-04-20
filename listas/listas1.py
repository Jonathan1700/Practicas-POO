estudiante = [
    {"nombre": "Elian Galeas", "nota": 10,},
    {"nombre": "jose torres", "nota": 2,} 
]

notas = list(map(lambda x: x["nota"], estudiante))
nombre_y_notas = list(map(lambda x:{"Nombre": x["nombre"], "calif": x["nota"]},estudiante))
print(notas)
print (nombre_y_notas)