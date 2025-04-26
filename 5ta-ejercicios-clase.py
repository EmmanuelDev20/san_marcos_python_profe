import os

os.system("clear")

# Clase sobre Funciones en Python

# Concepto de Funciones
"""
Una función en Python es un bloque de código reutilizable que realiza una tarea específica. 
Las funciones nos permiten organizar el código, hacerlo más legible y evitar la repetición.

Sintaxis básica de una función:
def nombre_funcion(parametros):
  # Cuerpo de la función
  return valor

- `def`: Palabra clave para definir una función.
- `nombre_funcion`: Identificador único para la función.
- `parametros`: Valores que la función puede recibir como entrada (opcional).
- `return`: Palabra clave para devolver un valor (opcional).
"""

# Ejemplo básico de una función
# def saludar(nombre):
#   return f"Hola, {nombre}!"

# Llamada a la función
# print(saludar("Emmanuel"))

# Ejemplo de función sin parámetros
# def mostrar_mensaje():
#   print("¡Bienvenidos a la clase de Python!")

# mostrar_mensaje()

# def decir_nombre():
#   print("Este es el curso web")

# decir_nombre()

# Ejemplo de función con múltiples parámetros
def sumar(num1, num2, num3=0, num4=3):
  print(num1 + num2 + num3 + num4)

# sumar(5, 3, 88, 99)
# sumar(2, 2)
# sumar(50, 39)
# sumar(500, 32)
# sumar(5, 123)
# sumar(52, 791234)
# print(sumar(5, 3))

# # Ejemplo de función con valor por defecto
# def potencia(base, exponente=2):
#   """Esta función calcula la potencia de un número."""
#   return base ** exponente

# print(potencia(3))  # Usa el valor por defecto del exponente
# print(potencia(2, 3))  # Sobrescribe el valor por defecto

# # Prácticas
# """
# 1. Escribe una función llamada `es_par` que reciba un número y devuelva `True` si es par y `False` si es impar.
# 2. Crea una función llamada `area_rectangulo` que reciba la base y la altura de un rectángulo y devuelva su área.
# 3. Define una función llamada `es_palindromo` que reciba una palabra y devuelva `True` si es un palíndromo y `False` en caso contrario.
# 4. Escribe una función llamada `calcular_promedio` que reciba una lista de números y devuelva el promedio.
# 5. Crea una función llamada `convertir_temperatura` que reciba una temperatura en Celsius y la convierta a Fahrenheit.
# """

def es_par(num1):
  print(num1 % 2 == 0)

es_par(5)
es_par(99)
es_par(9195)
es_par(9192)
es_par(9194)








# # Ejemplo de solución para una práctica
def es_par(numero):
  """Devuelve True si el número es par, False si es impar."""
  return numero % 2 == 0

# # Probando la función
# print(es_par(4))  # True
# print(es_par(7))  # False

# # Solución para calcular el área de un rectángulo
# def area_rectangulo(base, altura):
#   """Devuelve el área de un rectángulo dado su base y altura."""
#   return base * altura

# # Probando la función
# print(area_rectangulo(5, 10))  # 50
# print(area_rectangulo(3, 7))   # 21

# # Solución para verificar si una palabra es un palíndromo
# def es_palindromo(palabra):
#   """Devuelve True si la palabra es un palíndromo, False en caso contrario."""
#   palabra = palabra.lower().replace(" ", "")  # Ignorar mayúsculas y espacios
#   return palabra == palabra[::-1]

# # Probando la función
# print(es_palindromo("radar"))  # True
# print(es_palindromo("python"))  # False
# print(es_palindromo("anita lava la tina"))  # True

# # Solución para calcular el promedio de una lista de números
# def calcular_promedio(numeros):
#   """Devuelve el promedio de una lista de números."""
#   if not numeros:  # Evitar división por cero
#     return 0
#   return sum(numeros) / len(numeros)

# # Probando la función
# print(calcular_promedio([10, 20, 30, 40]))  # 25.0
# print(calcular_promedio([]))  # 0

# # Solución para convertir temperatura de Celsius a Fahrenheit
# def convertir_temperatura(celsius):
#   """Convierte una temperatura de Celsius a Fahrenheit."""
#   return (celsius * 9/5) + 32

# # Probando la función
# print(convertir_temperatura(0))  # 32.0
# print(convertir_temperatura(100))  # 212.0