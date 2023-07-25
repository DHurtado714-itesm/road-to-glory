class Pila:
    def __init__(self):
        self.elementos = []  # Iniciamos una lista vacía para almacenar los elementos de la pila.

    def push(self, dato):
        # La función append de las listas de Python añade el elemento al final de la lista,
        # que en nuestro caso equivale a la parte superior de la pila.
        self.elementos.append(dato)

    def pop(self):
        # Verificamos primero si la pila no está vacía.
        if not self.esta_vacia():
            # La función pop de las listas de Python retira el último elemento de la lista,
            # que en nuestro caso equivale a retirar el elemento de la parte superior de la pila.
            return self.elementos.pop()

    def esta_vacia(self):
        # Verificamos si la pila está vacía comprobando si la longitud de la lista es 0.
        return len(self.elementos) == 0

    def mostrar_pila(self):
        # Devolvemos la lista de elementos que conforma nuestra pila.
        return self.elementos
