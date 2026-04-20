def validar_peso(func):
    def wrapper (ejercicio,peso):
        if peso <= 0:
            print (f"error en {ejercicio}, el peso ({peso}kg) debe ser mayor a 1")
        else:
            return func(ejercicio,peso)
        return wrapper