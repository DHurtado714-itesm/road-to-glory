# Trabajando con Listas en Python

## 1. Creación de Listas:

```python
# Crear una lista vacía
lista_vacia = []

# Crear una lista con elementos
lista = [1, 2, 3, 4, 5]

# Acceder al primer elemento (índice 0)
primer_elemento = lista[0]

# Acceder al último elemento
ultimo_elemento = lista[-1]

# Modificar el primer elemento
lista[0] = 10

# Agregar un elemento al final de la lista
lista.append(6)

# Insertar un elemento en una posición específica (posición, valor)
lista.insert(1, 20)  # inserta el número 20 en la posición 1

# Eliminar un elemento por su valor
lista.remove(20)

# Eliminar un elemento por su índice y obtener su valor
elemento_eliminado = lista.pop(1)

# Eliminar un elemento por su índice
del lista[0]

# Obtener la longitud de la lista
longitud = len(lista)

# Ordenar la lista (ascendente por defecto)
lista.sort()

# Ordenar la lista en orden descendente
lista.sort(reverse=True)

# Invertir el orden de la lista
lista.reverse()

# Encontrar el índice de un elemento
indice = lista.index(3)  # Devuelve un error si el elemento no está en la lista

# Contar ocurrencias de un elemento
ocurrencias = lista.count(3)

# Obtener los primeros tres elementos
primeros_tres = lista[:3]

# Obtener los elementos del índice 2 al 4
sub_lista = lista[2:5]

# Obtener los últimos tres elementos
ultimos_tres = lista[-3:]
