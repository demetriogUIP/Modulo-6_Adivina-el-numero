from core_game import partida_juego

def main():
    print("==== ADIVINA EL NUMERO ====")

    while True:
        partida_juego()

        repuesta = input("\n¿Quieres jugar otra partida? (s/n): ").lower().strip()

        if repuesta != 's':
            print("\n¡Gracias por jugar! Adiós. 👋")
            break
        print("\n" + "="* 40 + "\n")

if __name__ == '__main__':
    main()