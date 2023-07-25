class Fila:
    def __init__(self):
        self.elementos = []  # Iniciamos una lista vacía para almacenar los elementos de la fila.

    def enqueue(self, dato):
        # La función insert de las listas de Python añade el elemento al inicio de la lista,
        # que en nuestro caso equivale a la parte trasera de la fila.
        self.elementos.insert(0, dato)

    def dequeue(self):
        # Verificamos primero si la fila no está vacía.
        if not self.esta_vacia():
            # La función pop de las listas de Python retira el último elemento de la lista,
            # que en nuestro caso equivale a retirar el elemento del frente de la fila.
            return self.elementos.pop()

    def esta_vacia(self):
        # Verificamos si la fila está vacía comprobando si la longitud de la lista es 0.
        return len(self.elementos) == 0

    def mostrar_fila(self):
        # Devolvemos la lista de elementos que conforma nuestra fila.
        return self.elementos
