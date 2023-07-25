def busqueda_binaria(lista, item_buscado):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        prediccion = lista[medio]
        if prediccion == item_buscado:
            return medio
        elif prediccion > item_buscado:
            alto = medio - 1
        else:
            bajo = medio + 1
    return None
