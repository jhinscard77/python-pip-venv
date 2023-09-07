import random

options = ("piedra", "papel", "tijera")


def choose_options():
    # Con la funcion lower convertimos a minuscula el dato ingresado
    user_option = (input("¿Piedra, papel o tijera?: ")).lower()

    if not user_option in options:
        print("Esa opción no es valida")
        # continue
        return None, None

    computer_option = random.choice(options)

    print("😀El usuario escogió:", user_option)
    print("💻La computadora escogió:", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡Empate de opción🤝🏻!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("La Piedra le gana a la Tijera")
            print("¡El usuario😀 ganó!")
            user_wins += 1
        else:
            print("El Papel le gana a la Piedra")
            print("¡El computador💻 ganó!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("El Papel le gana a la Piedra")
            print("¡El usuario😀 ganó!")
            user_wins += 1
        else:
            print("La Tijera le gana al papel")
            print("¡El computador💻 ganó!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("La Tijera le gana al papel")
            print("¡El usuario😀 ganó!")
            user_wins += 1
        else:
            print("El Papel le gana a la piedra")
            print("¡El computador💻 ganó!")
            computer_wins += 1
    print("Puntos 💻", computer_wins)
    print("Puntos 😀", user_wins)
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 1 and user_wins == 1:
            print("EMPATE DE PUNTOS! ¿Quién será el ganador?")

        if computer_wins == 2:
            print("El ganador es la computadora 💻")
            break
        if user_wins == 2:
            print("El ganador es el usuario 😁")
            break


run_game()
