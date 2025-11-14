import random

print("=== ADIVINA EL NÚMERO (Versión con limite de intentos y validaciones) ===")

# Genera número secreto entre 1 y 20(dificultad basica)
numero_secreto = random.randint(1, 20)

#Se limita la cantidad de intentos que puede tenr el jugador 
INTENTOS_MAXIMO = 5

# Elimino la variable adivinado porque usare un bucle for
# Variable para controlar si adivinaron
#adivinado = False

for intento in range(1, INTENTOS_MAXIMO + 1):
    print(f"\n--- Se encuentra en su Intento {intento} de {INTENTOS_MAXIMO} ---")

    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 20: "))
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")
            continue

        #agrego otra validacion mas que solo aplica para la dificultad basica
        if numero < 1 or numero > 20:
            print("El numero ingresado esta fuera de la dificultad seleccionada")
            continue

        break # Sale del bucle 'while True' al obtener una entrada válida y en rango

    if numero < numero_secreto:
        print("El número secreto es MAYOR.")
    elif numero > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        print("¡Correcto! Adivinaste el número.")
        # adivinado = True <-- Esta variable ya no existe y no es necesaria
        break # Rompe el bucle 'for' al adivinar

# Este es el 'else' del bucle 'for', se ejecuta si el 'for' termina sin un 'break'
else: 
    print(f"\nSe acabaron los intentos. El número secreto era: {numero_secreto}")