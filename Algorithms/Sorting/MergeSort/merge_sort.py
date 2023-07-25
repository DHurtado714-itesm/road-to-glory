# Este es como un juego de rompecabezas. Tienes todas las piezas mezcladas 
# y las divides por la mitad, luego divides cada mitad por la mitad, y así 
# sucesivamente hasta que solo tengas montones de una pieza. Ahora, tomas 
# dos montones, los ordenas y los juntas. Repites este proceso, siempre 
# tomando dos montones, ordenándolos y uniéndolos, hasta que todas las piezas 
# estén juntas y ordenadas.

def merge_sort(arr):
    # Si la lista está vacía o solo tiene un elemento, ya está ordenada.
    if len(arr) <= 1:
        return arr

    # Dividimos la lista a la mitad
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Ordenamos cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Ahora juntamos las mitades
    return merge(left_half, right_half)

def merge(left, right):
    # Esta función se encarga de juntar las listas
    result = []
    i = j = 0

    # Vamos recorriendo las dos listas
    while i < len(left) and j < len(right):
        # Si el elemento de la izquierda es menor, lo añadimos a la lista resultado
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # Si el elemento de la derecha es menor, lo añadimos a la lista resultado
        else:
            result.append(right[j])
            j += 1

    # Si todavía quedan elementos en alguna de las listas, los añadimos todos a resultado
    result.extend(left[i:])
    result.extend(right[j:])
    return result
