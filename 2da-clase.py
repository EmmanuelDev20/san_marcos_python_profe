# Operaciones aritmeticas

numero1 = 13
numero2 = "13"

# Suma
print(numero1 + numero2)

# Resta
print(numero1 - numero2)

# Multiplicacion
print(numero1 * numero2)

# Division
print(numero1 / numero2)

# Division entera
print(numero1 // numero2)

# Potencia
print(numero1 ** numero2)

# Modulo
print(numero1 % numero2)

# Operaciones de comparacion
# Retorna un Boolean = True / False

# Mayor que
print(numero1 > numero2)
# Menor que
print(numero1 < numero2)
# Mayor o igual que
print(numero1 >= numero2)
# Menor o igual que
print(numero1 <= numero2)
# Igual que
print(numero1 == numero2)
# Diferente de
print(numero1 != numero2)

# Operaciones logicas
# And
print(numero1 > numero2 and numero1 < 20)
# Or
print(numero1 > numero2 or numero1 < 20)


# Pide al usuario un número entero y conviértelo a flotante.
# Luego, conviértelo a cadena y muestra los valores resultantes con su tipo.
# "El número entero es: [variable] (tipo: [tipo de variable])"

# Solución:
entero = input("Ingresa un número entero: ")

print(f"El número es: {entero}")

try:
    entero = int(entero)
except ValueError:
    print("Por favor, ingresa un número entero válido.", ValueError)
else:
    flotante = float(entero)
    cadena = str(entero)
    print(f"El número entero es: {entero} (tipo: {type(entero)})")
    print(f"El número flotante es: {flotante} (tipo: {type(flotante)})")
    print(f"El número como cadena es: {cadena} (tipo: {type(cadena)})")


# Solicita una frase al usuario.
# Muestra la cantidad de caracteres.
# Imprime la frase en mayúsculas y en minúsculas.
# Muestra solo los primeros 5 caracteres.

frase = input("Ingresa una frase: ")
print(len(frase))
print(frase.upper())
print(frase.lower())