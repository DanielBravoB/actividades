import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanzas!")
    rango_inferior = int(input("Introduce el límite inferior del rango: "))
    rango_superior = int(input("Introduce el límite superior del rango: "))
    
    numero_secreto = random.randint(rango_inferior, rango_superior)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = int(input(f"Adivina el número (entre {rango_inferior} y {rango_superior}): "))
        intentos += 1
        
        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
            adivinado = True

if __name__ == "__main__":
    juego_adivinanza()
