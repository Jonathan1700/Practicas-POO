def pedido (**kwargs):
    print (f"contenido:{kwargs}")

pedido (comida = "salchipapa", salsa = "salsa de tomate", proteina = "pollo")

# todo lo que le damos al decorador **kwargs se convierte en un diccionario 