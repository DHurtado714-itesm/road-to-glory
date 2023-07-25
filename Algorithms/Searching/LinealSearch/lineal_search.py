def busqueda_lineal(lista, item_buscado):
    for i in range(len(lista)):
        if lista[i] == item_buscado:
            return i  # Devolvemos el índice si encontramos el ítem
    return None  # Si no encontramos el ítem, devolvemos None
