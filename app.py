# Juego de pierda, papel o tijera
# 1. El jugador escoge una opción
# 2. La computadora escoge una opción
# 3. Se determina el ganador
# 4. Se muestra el resultado
# 5. Se repite el proceso

from random import randint

opciones = ['piedra', 'papel', 'tijera']

def quien_gana(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif jugador == 'piedra' and computadora == 'tijera':
        return "Gana el jugador"
    elif jugador == 'papel' and computadora == 'piedra':
        return "Gana el jugador"
    elif jugador == 'tijera' and computadora == 'papel':
        return "Gana el jugador"
    else:
        return "Gana la computadora"

print("Bienvenido al juego de piedra, papel o tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("4. Salir")

while True:
    jugador = input("Seleccione una opción: ").lower()

    if jugador == 'salir' or jugador == '4':
        break

    if jugador not in opciones:
        print("Opción inválida")
        continue

    computadora = opciones[randint(0,2)]

    print("Computadora: " + computadora)

    print(quien_gana(jugador, computadora))
