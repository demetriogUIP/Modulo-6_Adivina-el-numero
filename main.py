import random

print("=== ADIVINA EL NÚMERO (Versión básica) ===")

# Genera número secreto entre 1 y 20
numero_secreto = random.randint(1, 20)

# Variable para controlar si adivinaron
adivinado = False

while not adivinado:
    try:
        numero = int(input("Ingresa un número entre 1 y 20: "))
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número.")
        continue

    if numero < numero_secreto:
        print("El número secreto es MAYOR.")
    elif numero > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        print("¡Correcto! Adivinaste el número.")
        adivinado = True
