# nombre = "Kevin" # String Texto
# edad = 55 # int Entero
# temperatura = 36.3 # float decimal
# esMayorDeEdad = True # bool True / False

# print(type(nombre), type(edad), type(temperatura), type(esMayorDeEdad))

# print(edad - temperatura)


nombre = input("Por favor ingresa tu nombre ")
edad = int(input("Cual es tu edad? "))
temperatura = float(input("Cual es tu temperatura "))
esMayorDeEdad = edad > 17 # True / False
# esMayorDeEdad = input("Eres mayor de edad? Si o No?") == "Si"

# print("Hola " + nombre +  " " + " tu edad es" + " " + str(edad) + " tu temperatura es " + str(temperatura) + " es mayor de edad " + str(esMayorDeEdad) )

print(f"Hola {nombre} tu edad es {edad} tu temperatura es {temperatura} es mayor de edad {esMayorDeEdad}")
