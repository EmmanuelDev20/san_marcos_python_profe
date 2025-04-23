import os
os.system("clear")

# message = 'Hola mundo!'

# print(message[0])

# name = 'Emmanuel'
# last_name = 'Ovares'

# 1. Unir texto
# full_name = name + last_name + str(30) + 'anos'

# 2. Unir texto
# full_name = ' '.join([name, last_name])

# 3. Unir texto
# full_name = 'El nombre completo es: %s %s y tiene 30 anhos' %(name, last_name)

# # 4. Unir texto format
# base = 'El nombre completo es: {} {}'
# full_name = base.format(name, last_name)

# # Format con nombres
# base = 'El nombre completo es: {name} {last_name}'
# full_name = base.format(
#   name=name,
#   last_name=last_name,
#   age=30
# )

# print(full_name)

# name = input('Ingresa tu nombre')
# last_name = input('Ingresa tu apellido')
# age = input('Ingresa tu edad')

# # full_name = base.format(name, last_name, age)
# print(full_name)

# 5. Unir texto f string
# full_name = f'Hola {name}, este es tu apellido {last_name}'

"""
!Explicación de los ejemplos de código
"""
# edad = int(input("Que edad tienes?"))

# print(type(edad))

# if edad >= 18:
#   print('Puedes ingresar.')
# else:
#   print('Aun no eres mayor de edad.')

# edad = int(input("Cual es tu edad?"))
# tieneDinero = input("tienes dinero para pagar?")

# if tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'sí tengo' or tieneDinero.lower() == 'si':
#   if edad > 18:
#     print('Comida McDonalds')
#   else:
#     print('Comida saludable')
# elif tieneDinero.lower() == 'no, pero me regalas':
#   print('Ok, no hay problema. Toma.')
# else:
#   print('No podemos entregar tu comida')

# if (tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'si') and edad >= 18:
#   print('Comida McDonalds')
# elif (tieneDinero.lower() == 'si tengo' or tieneDinero.lower() == 'si') and edad < 18:
#   print('Comida saludable')
# elif tieneDinero.lower() == 'no, pero me regalas':
#   print('Ok, no hay problema. Toma.')
# else:
#   print('No podemos entregar tu comida')

# if edad > 18:
#   print('Comida McDonalds')
# else:
#   print('Comida saludable')

# Escribe un programa que pida al usuario un número y luego imprima si el número es 
# positivo, negativo o cero

# num = input("Ingrese un numero")

# try:
#   num = int(num)
# except ValueError:
#   print('Por favor ingresa un numero valido ')

# numero_cualquiera = 88

# for i in range(5):
#   print("Hola a todos" + str(i))
#   print("Hola mi gente" + str(i))
#   print("Estamos en desarrollo web" + str(i))
#   numero_cualquiera = numero_cualquiera + 1
#   print('este: ', str(numero_cualquiera))

# print(numero_cualquiera)

# Imprima en consola los numeros del 1 al 100

# for i in range(10):
#   print(f'9 x {i + 1} = {9 * (i + 1)}')

# for i in range(6, 10):
#   print(i)

# contador = 0

# while contador < 5:
#   print('Contador' + str(contador))
#   contador = contador + 1

# jugando = True

# while jugando == True:
#   print('Seguimos en el juego')
#   jugando = False


# Solicitar un valor al usuario y retornar si el valor es par o impar
input("Ingresa cualquier numero")















# # Example of if condition
# # Explanation: The `if` statement is used to execute a block of code only if a specified condition is true.
# age = 18
# if age >= 18:
#   print("You are an adult.")
# else:
#   print("You are a minor.")

# # Example of for loop
# # Explanation: The `for` loop is used to iterate over a sequence (like a list, tuple, or string).
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(f"I like {fruit}")
#   print('Hello my people')

# # Example of while loop
# # Explanation: The `while` loop is used to execute a block of code as long as a condition is true.
# count = 0
# while count < 5:
#   print(f"Count is {count}")
#   count += 1

# # Example of try-except
# # Explanation: The `try-except` block is used to handle exceptions (errors) in the code.
# try:
#   number = int(input("Enter a number: "))
#   print(f"You entered: {number}")
# except ValueError:
#   print("That's not a valid number!")