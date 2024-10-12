import random

# Función para validar la entrada de jugadores
def solicitar_numero_jugadores():
    while True:
        try:
            num_jugadores = input("Ingresa la cantidad de jugadores (2-4): ")
            
            # Verifica si es un número
            if not num_jugadores.isdigit():
                print("Error: Por favor ingresa un número válido.")
                continue
            
            # Convierte a entero
            num_jugadores = int(num_jugadores)
            
            # Verifica si está dentro del rango permitido
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                print("Debe haber entre 2 y 4 jugadores.")
        except ValueError:
            print("Por favor ingresa un número válido.")

# Función para solicitar el nivel de tablero
def solicitar_nivel_tablero():
    print("\nSelecciona el nivel de tablero:")
    print("1. Nivel básico (20 posiciones)")
    print("2. Nivel intermedio (30 posiciones)")
    print("3. Nivel avanzado (50 posiciones)")
    print("4. Nivel experto (100 posiciones)")
    
    while True:
        try:
            nivel = int(input("Ingresa el número del nivel (1-4): "))
            if nivel == 1:
                return 20
            elif nivel == 2:
                return 30
            elif nivel == 3:
                return 50
            elif nivel == 4:
                return 100
            else:
                print("Por favor selecciona una opción válida (1-4).")
        except ValueError:
            print("Por favor ingresa un número válido.")

# Función para lanzar dos dados y verificar pares consecutivos
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para el desarrollo del juego
def jugar():
    num_jugadores = solicitar_numero_jugadores()
    tablero = solicitar_nivel_tablero()
    posiciones = [0] * num_jugadores  # Posiciones de los jugadores
    pares_consecutivos = [0] * num_jugadores  # Contador de pares consecutivos

    juego_terminado = False
    
    while not juego_terminado:
        for i in range(num_jugadores):
            input(f"\nTurno del Jugador {i+1}. Presiona Enter para lanzar los dados...")
            dado1, dado2 = lanzar_dados()
            total = dado1 + dado2
            print(f"Jugador {i+1} ha lanzado: {dado1} y {dado2} (Total: {total})")
            
            if dado1 == dado2:
                pares_consecutivos[i] += 1
                print(f"Jugador {i+1} ha sacado un par! (Pares consecutivos: {pares_consecutivos[i]})")
                
                if pares_consecutivos[i] == 3:
                    print(f"¡Jugador {i+1} ha ganado automáticamente por obtener 3 pares consecutivos!")
                    juego_terminado = True
                    break
            else:
                pares_consecutivos[i] = 0

            # Avanza posiciones
            posiciones[i] += total
            print(f"Jugador {i+1} avanza {total} posiciones. Ahora está en la posición {posiciones[i]}.")

            # Verifica si ha alcanzado o superado la meta
            if posiciones[i] >= tablero:
                print(f"¡Jugador {i+1} ha llegado a la meta y gana el juego!")
                juego_terminado = True
                break

if __name__ == "__main__":
    jugar()


