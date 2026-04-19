class cuenta_banco:
    def __init__(self, nombre, saldo = 0):
        self.nombre = nombre
        self.saldo = saldo

    def consultar_saldo (self):
        return (f"EL usuario {self.nombre} tiene un saldo de {self.saldo}$ en su cuenta")
    
    def crear_depositos (self, monto):
        if monto == 0:
            print (f" Ingrese un monto ")
        else:
            self.saldo += monto
            print (F" Su deposito de {monto} a sido acreditado con exito, ahora tiene un saldo de {self.saldo}")
    
    def hacer_retiros(self, monto_r):
        if monto_r > self.saldo:
            print (f"no tienes el suficiente saldo para hacer este retiro")
        else:
            self.saldo -= monto_r
            print (f"ha retirado un monto de {monto_r} y su nuevo saldo es {self.saldo}")
        

cuenta = cuenta_banco("jose", 400)
cuenta.crear_depositos(50)
cuenta.hacer_retiros(20)
cuenta.crear_depositos(50)
print(cuenta.consultar_saldo())
        