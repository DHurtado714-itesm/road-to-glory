# Imagina que tienes una fila de personas de diferentes alturas y 
# quieres ordenarlas de la más baja a la más alta. Lo que haces es 
# comenzar desde el principio de la fila, comparar a cada par de 
# personas adyacentes y si la persona a la derecha es más baja que 
# la persona a la izquierda, les pides que intercambien lugares. 
# Sigues haciendo esto una y otra vez, recorriendo toda la fila, 
# hasta que ya no necesites hacer más intercambios. Ahora tienes 
# a todas las personas ordenadas de la más baja a la más alta.


def bubble_sort(lista):
    n = len(lista)

    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Queremos que el último i elementos ya estén en orden
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                # Entonces intercambiamos los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
