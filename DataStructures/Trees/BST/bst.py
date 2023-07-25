class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo_actual):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(dato)
            else:
                self._insertar(dato, nodo_actual.izquierdo)
        elif dato > nodo_actual.dato:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(dato)
            else:
                self._insertar(dato, nodo_actual.derecho)
        else:
            print("El dato ya está en el árbol")

    # Puedes agregar métodos adicionales para buscar, eliminar nodos, etc.
