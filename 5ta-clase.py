import os
os.system("clear")

import math

# Una función es un bloque de código que realiza una tarea específica. Permite reutilizar
# código, organizarlo mejor y hacerlo más fácil de leer y mantener.

# Usar nombres descriptivos para las funciones y los parámetros.
# Evitar repetir código innecesariamente.
# Documentar cada función con comentarios o docstrings.

# Funciones en javascript
# function saludar() {

# }

# variable1 = 55

# def saludar():                #1 encuentra la funcion
#   print('hola mi gente')      #2 imprimir hola mi gente
#   print('hola mi gente')      #2 imprimir hola mi gente
#   print('hola mi gente')      #2 imprimir hola mi gente
#   print('hola mi gente')      #2 imprimir hola mi gente
#   print('hola mi gente')      #2 imprimir hola mi gente
#   print('hola mi gente')      #2 imprimir hola mi gente
#   return 55                   #3 retorna el valor de 55
#   print('asfdasjpfdsafd')
#   print('asfdasjpfdsafd')
#   print('asfdasjpfdsafd')
#   print('asfdasjpfdsafd')
#   print('asfdasjpfdsafd')
#   print('asfdasjpfdsafd')

# saludar()
# print(saludar())

# edad = 18

# def mayorEdad():
#   if edad >= 18:
#     return 'Edad 18'
  
#   if edad > 23:
#     return 'Edad 23'
  
#   if edad > 55:
#     return 'Edad 55'
#   # else:
#   #   return 'no puedes pasar'
#   return 'hola'

# print(mayorEdad())

# def saludar():
#   # print('hola mi gente')
#   return 55
#   print('hola mi gente despues del return')
#   print('hola mi gente despues del return')
#   print('hola mi gente despues del return')
#   print('hola mi gente despues del return')
#   print('hola mi gente despues del return')
#   print('hola mi gente despues del return')

# print(saludar())
# saludo1 = saludar()
# saludo2 = saludar()

# print('saludo 1', saludo1)
# print('saludo 2', saludo2)

# Definición de una función simple
# def saludar():
#               """Esta función imprime un saludo."""
#               print("¡Hola! Bienvenido a la clase de Python.")

# # Llamada a la función
# saludar()

# # Función con parámetros
# def saludar(nombre, tecnico, edad):
#   return f'{nombre} del tecnico {tecnico} de {edad}'

# print(saludar('Emmanuel', 'Web', 30))
# print(saludar('Luis', 'Web', 30))
# print(saludar('Christian', 'Web', 30))

# def sumar(a, b):
#   """Esta función toma dos números y devuelve su suma."""
#   return a + b

# # # Uso de la función con parámetros
# resultado = sumar(5, 3)
# print(f"La suma de 5 y 3 es: {resultado}")

# # Función con valores por defecto
# def presentar(nombre='Mariano', edad=18):
#   """Esta función presenta a una persona con un nombre y una edad."""
#   print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# # Llamada a la función con y sin el valor por defecto
# presentar("Emmanuel", 25)
# presentar("Ana")
# presentar()

# # Función con retorno múltiple
# def operaciones_basicas(a, b):
#   """Esta función devuelve la suma, resta, multiplicación y división de dos números."""
#   suma = a + b
#   resta = a - b
#   multiplicacion = a * b
#   division = a / b if b != 0 else "Indefinido"
#   return suma, resta, multiplicacion, division

# # print(operaciones_basicas(10, 2))
# # print(operaciones_basicas(8, 2))
# # print(operaciones_basicas(19, 2))
# # print(operaciones_basicas(20, 2))
# # # Uso de la función con retorno múltiple
# suma, resta, multiplicacion, division = operaciones_basicas(10, 2)
# print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# # Función lambda (anónima)
# doblar = lambda x: x * 2
# print(f"El doble de 4 es: {doblar(4)}")

# Ejercicio 1: Crear una función que calcule el área de un círculo dado su radio. (Debe devolver el área)

# def presentar(nombre='Mariano', edad=18):
#   """Esta función presenta a una persona con un nombre y una edad."""
#   print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# radio ** 2 * pi

# Opcion 1
# def calcularArea(radio):
#   return radio ** 2 * 3.14

# Opcion 2
# def calcularArea(radio):
#   pi = 3.14
#   return radio ** 2 * pi

# Opcion 3
# def calcularArea(radio):
#   pi = 3.14
#   return radio ** 2 * pi

# Opcion 4
# def calcularArea():
#   radio = int(input("Ingresa el radio: "))
#   pi = 3.14
#   return radio ** 2 * pi

# Opcion 5
def calcularArea():
  radio = int(input("Ingresa el radio: "))
  pi = 3.14
  msg = f'El area del circulo es: {radio ** 2 * pi}'
  return msg

# radioUsuario = int(input("Ingresa el radio: "))
print(calcularArea())


# Ejercicio 2: Crear una función que determine si un número es par o impar. 
# Recibir el numero como parametro.
# (Debe devolver True o False)
# numero % 2 == 0
# Imprimir el resultado












# Ejercicio 3: Crear una función que reciba una lista de números y devuelva la suma de sus elementos. (Debe devolver la suma)
# Ejercicio 4: Crear una función que reciba una cadena y devuelva la misma cadena en mayúsculas. (Debe devolver la cadena en mayúsculas)































# # Ejercicio 1: Crear una función que calcule el área de un círculo dado su radio.
# def area_circulo(radio):
#   """Devuelve el área de un círculo dado su radio."""
#   return 3.14159 * radio ** 2

# # Ejercicio 2: Crear una función que determine si un número es par o impar.
# def es_par(numero):
#   """Devuelve True si el número es par, de lo contrario False."""
#   return numero % 2 == 0

# # Ejercicio 3: Crear una función que reciba una lista de números y devuelva la suma de sus elementos.
# def suma_lista(lista):
#   """Devuelve la suma de los elementos de una lista."""
#   return sum(lista)

# # Ejercicio 4: Crear una función que reciba una cadena y devuelva la misma cadena en mayúsculas.
# def convertir_mayusculas(cadena):
#   """Devuelve la cadena en mayúsculas."""
#   return cadena.upper()
