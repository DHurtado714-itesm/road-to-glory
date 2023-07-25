# Imagina que estás jugando un juego de cartas. Escoges una carta al azar, 
# la llamaremos "pivote". Luego, divides todas las demás cartas en dos montones: 
# uno con todas las cartas menores al pivote y otro con todas las cartas mayores. 
# Ahora, repites el mismo juego para cada montón, eligiendo un nuevo "pivote" y 
# dividiéndolas hasta que solo tengas montones de una carta. ¡Felicitaciones! Ahora 
# todas tus cartas están ordenadas.


def quicksort(arr):
    # Si la lista está vacía o solo tiene un elemento, ya está ordenada.
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Elegimos un pivote
        left = [x for x in arr if x < pivot]  # Todos los elementos menores al pivote
        middle = [x for x in arr if x == pivot]  # Todos los elementos iguales al pivote
        right = [x for x in arr if x > pivot]  # Todos los elementos mayores al pivote
        # Ahora ordenamos cada parte y las unimos
        return quicksort(left) + middle + quicksort(right)
    

