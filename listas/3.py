def listas(self) -> None:
        """
        CONCEPTO:
        Listas son estructuras mutables.

        IMPORTANTE:
        - métodos: append, pop, sort
        """

lista = [10, 5, 8]

lista.append(20)
lista.sort()
print(lista)

        # EJERCICIO
print(sum(lista))
print(max(lista))

print(lista.pop(2))
print (lista)