# Definimos la clase Nodo, que será la unidad básica de nuestro árbol.
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Cada nodo almacena un dato.
        self.izquierdo = None  # Referencia al nodo hijo izquierdo. Inicia como None.
        self.derecho = None  # Referencia al nodo hijo derecho. Inicia como None.

# Definimos la clase ArbolBinario, que contendrá todos los nodos.
class ArbolBinario:
    def __init__(self):
        self.raiz = None  # La raíz del árbol. Inicia como None.

    # Método para agregar nodos al árbol.
    def agregar_nodo(self, dato):
        if not self.raiz:  # Si el árbol está vacío...
            self.raiz = Nodo(dato)  # ... creamos un nuevo nodo y lo asignamos como la raíz.
        else:  # Si el árbol no está vacío...
            self._agregar_nodo(dato, self.raiz)  # ... llamamos al método privado _agregar_nodo.

    # Método privado para agregar nodos al árbol de manera recursiva.
    def _agregar_nodo(self, dato, nodo_actual):
        if dato < nodo_actual.dato:  # Si el dato es menor que el dato del nodo actual...
            if nodo_actual.izquierdo is None:  # ... y si no hay nodo hijo izquierdo...
                nodo_actual.izquierdo = Nodo(dato)  # ... creamos un nuevo nodo y lo asignamos como hijo izquierdo.
            else:  # Si ya hay un nodo hijo izquierdo...
                self._agregar_nodo(dato, nodo_actual.izquierdo)  # ... llamamos recursivamente al método _agregar_nodo para el nodo hijo izquierdo.
        else:  # Si el dato es mayor o igual que el dato del nodo actual...
            if nodo_actual.derecho is None:  # ... y si no hay nodo hijo derecho...
                nodo_actual.derecho = Nodo(dato)  # ... creamos un nuevo nodo y lo asignamos como hijo derecho.
            else:  # Si ya hay un nodo hijo derecho...
                self._agregar_nodo(dato, nodo_actual.derecho)  # ... llamamos recursivamente al método _agregar_nodo para el nodo hijo derecho.
