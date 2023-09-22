# Trabajando con Strings en Python

## 1. Creación de Strings:

```python
# Crear una cadena de caracteres
cadena = "Hola, mundo!"

# Crear una cadena multi-línea
cadena_multilinea = """
Hola,
mundo!
"""

# Acceder al primer carácter
primer_caracter = cadena[0]

# Acceder al último carácter
ultimo_caracter = cadena[-1]

# Obtener los primeros cinco caracteres
primeros_cinco = cadena[:5]

# Obtener los caracteres del índice 6 al 10
sub_cadena = cadena[6:11]

# Obtener los últimos tres caracteres
ultimos_tres = cadena[-3:]

# Convertir la cadena a mayúsculas
mayusculas = cadena.upper()

# Convertir la cadena a minúsculas
minusculas = cadena.lower()

# Verificar si la cadena empieza con una subcadena específica
empieza_con = cadena.startswith("Hola")

# Verificar si la cadena termina con una subcadena específica
termina_con = cadena.endswith("mundo!")

# Encontrar la posición de una subcadena
posicion = cadena.find("mundo")

# Reemplazar una subcadena por otra
reemplazado = cadena.replace("mundo", "Python")

# Obtener la longitud de la cadena
longitud = len(cadena)

# Dividir la cadena por espacios (por defecto)
dividido = cadena.split()

# Dividir la cadena por una subcadena específica
dividido_coma = cadena.split(',')

# Unir una lista de cadenas en una sola cadena
unido = ' '.join(['Hola', 'mundo!'])

# Usar caracteres de escape, como las comillas dobles
cadena_con_comillas = "Ella dijo: \"¡Hola, mundo!\""

nombre = "Ana"
edad = 30

# Usando f-strings (Python 3.6+)
mensaje = f"{nombre} tiene {edad} años."

# Usando str.format()
mensaje_format = "{} tiene {} años.".format(nombre, edad)

