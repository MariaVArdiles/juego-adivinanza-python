nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input("¡Hola Jugador1 ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
jugador2 = input("¡Hola Jugador2 ¿Qué eliges? ¿Piedra, papel o tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)
