class producto:
    def __init__(self, nombre, precio, stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def agregar_stock(self,cantidad):
        if cantidad <= 0:
            print (f"ingrese una cantidad validad")
        else:
            self.stock += cantidad
            print (f"su stock ha sido actualizado con exito con una cantidad de {cantidad} unidades")
    
    def vender_producto(self, venta):
        if self.stock <= venta:
            print (f"No hay stock suficiente para realizar la venta")
        else:
            self.stock -= venta
            print (f"Usted ha vendido una cantidad de {venta}")
    
    def decuento (self, descuento):
        descuento = self.precio * (descuento/100)
        self.precio -= descuento
        print (f"se aplico un descuento del {descuento}%. y el nuevo precio es {self.precio}")
    

    def ver_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")
    

p = producto ("laptop", 600)
p.agregar_stock(20)
p.vender_producto(5)
p.vender_producto(30)
p.decuento(25)
p.ver_info()


