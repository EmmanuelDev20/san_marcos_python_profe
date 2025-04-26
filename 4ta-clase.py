import os

os.system("clear")

# Listas - Arrays - Arreglos

# """
# Listas en Python
# Tipo list
# <variable> = []
# """
#                 0                    1                2            3                
# tareas = ["Barrer la casa", "Acomodar el cuarto", "Cocinar", "Lavar la ropa"]

# tareas.append("Barrer el patio")

# print(tareas)

# print(len(tareas))
# print(tareas[6])

# for tarea in tareas:
#   print(tarea)

# for i in range(len(tareas)):
#   print(tareas[i])

# my_list = ["String", 10, 3.14, True, ["String", 10, 3.14, True]]

# my_list = [["string", [[], []]], "String", 10, 3.14, True, ["String", 10, 3.14, True]]
# # print(my_list)
# print(type(my_list))
#             0         1         2          3          4
# courses = ['History', 'Math', 'Physics', 'CompSci', 'Spanish']

# print(len(courses))

# courses_copy = courses[:]
# print(courses_copy)
# print(courses[2])
# print(courses[-1])
# print(courses[2:])
# print(courses[1:4])
# print(courses[2:])
# print(courses[1:])

# Reemplazar valores
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses[0] = 'Art'
# print(courses)

# Sublista
# courses = ['History', 'Math', 'Physics', 'CompSci', 'Art']
# sub_courses = [courses[0], courses[1], courses[2]]
# sub_courses = courses[:3]

# print(sub_courses)

# sub_courses = courses[0:3]
# sub_courses = courses[:]
# sub_courses = courses[::3] # Saltos de 2 en 2
# sub_courses = courses[::-2] # Dar la vuelta a la lista

# print(sub_courses)

# Agregar elementos
# courses.append('Art new') # Agrega al final

# courses.insert(2, 'Art new position') # Agrega en una posición específica
# print(courses)

# courses.insert(2, 'Otro arte') # Agrega en una posición específica
# print(courses)

# courses = ['History', 'Math', 'Physics', 'CompSci']

# courses.append('React') 
# new_courses = ['React', 'Angular', 'Astro']
# courses.extend(new_courses) # Agrega una lista a otra lista

# print(courses)

# print("Python" in courses) # False
# print("Math" in courses) # True
# print(courses.index('Math')) # 1 Si error falla, nos devuelve error

# courses.remove('Math') # Elimina un elemento de la lista
# courses.pop() # Elimina el último elemento de la lista
# courses.pop(courses.index('Math')) # Elimina el elemento en la posición 0
# print(courses)
# last_element = courses.pop() # Elimina el último elemento y lo guarda en una variable

# courses.clear() # Elimina todos los elementos de la lista

# print(courses)

# # copy, reverse, sort
# courses = [9, 2, 88, 1]
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses3 = courses[:]
# courses2 = courses.copy() # Es igual a courses[:]
# courses.reverse() # AL USAR ESTO SE MODIFICA LA LISTA ORIGINAL, CON SLICING NO courses[::-1] 
# courses.sort() # Ordena la lista
# courses.sort() # Ordena la lista de forma inversa

# print(courses[::-1])
# print(courses)
#             0          1          2
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#         0  1  2
# matrix = [1, 2, 3]

# matrix = [
#           [1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#         ]

# print(matrix[1][1])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8])

# Lista de strings de carros con longitud de 10

# ['Ford', 'Mitsubishi', 'Mercedes']
# carros = ['Toyota', 'Nissan', 'Ford', 'Volkswagen', 'Chevrolet', 'Mitsubishi', 'Hyundai', 'Kia', 'Mazda', 'Mercedes']

# print([carros[2], carros[5], carros[-1]])
# # Genera una sub lista con los 3 primeros y últimos elementos
# sub_carros = carros[:3]
# sub_carros.extend(carros[-3:])
# # sub_carros = carros[:3], carros[-3:]

# print(sub_carros)






# Ejercicio 1: Crear una lista de nombres y verificar si un nombre específico está en la lista.
# names = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis']

# validar_nombre = input("Escribe el nombre para validar")

# print(validar_nombre in names)

# # Ejercicio 2: Crear una lista de números y calcular la suma de todos los elementos.
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for number in numbers:
#   total = total + number
  # total += number

# for number in numbers:
#   total = total + number

# for u in range(len(numbers)):
#   total = total + numbers[u]

# ¿Como funciona el for?
# # 1 iteracion
# for 10 in numbers:
#   total = 0 + 10

# # 2 iteracion
# for 20 in numbers:
#   total = 10 + 20

# # 3 iteracion
# for 30 in numbers:
#   total = 30 + 30

# # 4 iteracion
# for 40 in numbers:
#   total = 60 + 40

# # 5 iteracion
# for 50 in numbers:
#   total = 100 + 50

# print(total)

# # Ejercicio 5: Crear una lista de números y eliminar todos los números impares.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# solo_pares = numbers[1::2]
# print(solo_pares)

# for number in numbers:
#   if number % 2 == 1:
#     numbers.remove(number)


# print(numbers)


# # Ejercicio 6: Crear una matriz 3x3 y mostrar el texto "matrix".
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, "matrix", 9]
# ]

# # Ejercicio 7: Crear una lista de frutas y ordenarlas alfabéticamente.
# fruits = ['Manzana', 'Banana', 'Cereza', 'Durazno']

# # Ejercicio 8: Crear una lista de números y duplicar cada elemento.
# numbers = [1, 2, 3, 4, 5]


# # Ejercicio 9: Crear una lista de 10 elementos y dividirla en dos sublistas iguales.

# # Ejercicio 10: Crear una lista de palabras y filtrar solo las palabras que tienen más de 5 letras.
# words = ['Python', 'Java', 'C++', 'JavaScript', 'HTML']


# # # # Carrito de compras usando listas
# # # cart = []

# # # def add_item(cart, item_name, price, quantity=1):
# # #     # Buscar si el producto ya está en el carrito
# # #     for item in cart:
# # #         if item[0] == item_name:
# # #             item[2] += quantity  # Incrementar la cantidad
# # #             return
# # #     # Si no está, agregarlo como una nueva entrada
# # #     cart.append([item_name, price, quantity])

# # # def remove_item(cart, item_name, quantity=None):
# # #     for item in cart:
# # #         if item[0] == item_name:
# # #             if quantity is None or item[2] <= quantity:
# # #                 cart.remove(item)  # Eliminar el producto
# # #             else:
# # #                 item[2] -= quantity  # Reducir la cantidad
# # #             return

# # # def calculate_total(cart):
# # #     return sum(item[1] * item[2] for item in cart)

# # # def show_cart(cart):
# # #     if not cart:
# # #         print("Your cart is empty.")
# # #     else:
# # #         print("Your cart contains:")
# # #         for item in cart:
# # #             print(f"- {item[0]}: ${item[1]} x {item[2]}")

# # # def clear_cart(cart):
# # #     cart.clear()
# # #     print("Your cart has been cleared.")

# # # # Ejemplo de uso
# # # add_item(cart, "Apple", 0.5, 3)
# # # add_item(cart, "Banana", 0.3, 5)
# # # add_item(cart, "Apple", 0.5, 2)  # Incrementa la cantidad de manzanas
# # # show_cart(cart)
# # # print(f"Total: ${calculate_total(cart):.2f}")
# # # remove_item(cart, "Banana", 2)  # Elimina 2 bananas
# # # show_cart(cart)
# # # clear_cart(cart)
# # # show_cart(cart)