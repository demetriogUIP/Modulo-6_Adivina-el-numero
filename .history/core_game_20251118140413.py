import random

print("=== ADIVINA EL NUMERO (Version con limite de intentos y validaciones) ===")

# ================================
# INTEGRANTE 3 – NIVELES DE DIFICULTAD (John)
# ================================
def seleccionar_dificultad():
    print("\nSelecciona un nivel de dificultad:")
    print("1. Facil   (1 - 10)")
    print("2. Medio   (1 - 20)")
    print("3. Dificil (1 - 50)")

    while True:
        opcion = input("Elige 1, 2 o 3: ")

        if opcion == "1":
            return 1, 10, "Facil"
        elif opcion == "2":
            return 1, 20, "Media"
        elif opcion == "3":
            return 1, 50, "Dificil"
        else:
            print("❌ Opcion invalida. Intenta nuevamente.")

def partida_juego():

    # Obtenemos el rango según la dificultad elegida
    MINIMO, MAXIMO, nombre_dificultad = seleccionar_dificultad()
    print(f"\nHas elegido dificultad: {nombre_dificultad}.")
    print(f"Piensa en un numero entre {MINIMO} y {MAXIMO}.\n")
    # ================================

    # Genera número secreto entre 1 y 20 (dificultad básica → ahora según dificultad)
    numero_secreto = random.randint(MINIMO, MAXIMO)

    # Se limita la cantidad de intentos que puede tener el jugador
    INTENTOS_MAXIMO = 5

    # Elimino la variable adivinado porque usaré un bucle for
    # Variable para controlar si adivinaron
    # adivinado = False

    for intento in range(1, INTENTOS_MAXIMO + 1):
        print(f"\n--- Se encuentra en su intento {intento} de {INTENTOS_MAXIMO} ---")

        while True:
            try:
                # antes: "Ingresa un número entre 1 y 20"
                numero = int(input(f"Ingrese un numero entre {MINIMO} y {MAXIMO}: "))
            except ValueError:
                print("Entrada invalida. Por favor ingresa un numero.")
                continue

            # agrego otra validación más que solo aplica para la dificultad básica
            # antes: if numero < 1 or numero > 20:
            if numero < MINIMO or numero > MAXIMO:
                print("El numero ingresado esta fuera de la dificultad seleccionada")
                continue

            # Sale del bucle 'while True' al obtener una entrada válida y en rango
            break

        if numero < numero_secreto:
            print("El numero secreto es MAYOR.")
        elif numero > numero_secreto:
            print("El numero secreto es MENOR.")
        else:
            print("¡Correcto! Adivinaste el numero.")
            # adivinado = True  # Esta variable ya no existe y no es necesaria
            # Rompe el bucle 'for' al adivinar
            break

    # Este es el 'else' del bucle 'for', se ejecuta si el 'for' termina sin un 'break'
    else:
        print(f"\nSe acabaron los intentos. El numero secreto era: {numero_secreto}")
