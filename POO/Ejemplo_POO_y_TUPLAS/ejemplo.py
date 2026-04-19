class personaje:
    def __init__(self, nombre, mana, habilidades, ulti, coste):
        self.nombre = nombre
        self.mana = mana 
        self.habilidades = habilidades
        self.ulti = ulti
        self.coste = coste
     

    def atacar (self, objetivo):
        if self.mana >= self.coste:
           self.mana -= self.coste
           return f"{self.nombre} ataca a {objetivo} con su habilidad {self.habilidades}y su mana se reduce a {self.mana}"
        else:
           return f"{self.nombre} no tiene mana"
    
    
viego = personaje ("viego",100,"rompecorazones", "stun", 50 )
print (viego.atacar("locotron"))