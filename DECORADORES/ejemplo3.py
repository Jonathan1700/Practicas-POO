def anotacion(funcion):
    def anotar (*args, **kwargs):
        print ("abriendo la libreta")

        if args:
            print(f"basicos del dia:{args}")

        if kwargs:
            print (f"detalles tecnicos: {kwargs}")

        print ("todo registrado")
        return funcion (*args, **kwargs)
    
    return anotar

@anotacion
def entrenar (*args, **kwargs):
    print ("entrenamiento completado")
@anotacion
def preparar (*args, **kwargs):
    print ("comida lista")

entrenar ("ejercicio1", "ejercicio2")
entrenar ("press banca", series =4, repes =8, peso=80)

preparar ("Pollo", "Huevos", gramos_arroz=250, calorias=850)