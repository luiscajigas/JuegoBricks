import random

def adivina_el_numero(simulacion=None):
    numero_secreto = random.randint(1, 100)
    intentos = 0
    for intento in simulacion or []:
        intentos += 1
        print(f"Intento {intentos}: {intento}")
        if intento < numero_secreto:
            print("Muy bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Muy alto, intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            return
    print(f"El número secreto era {numero_secreto}.")

# Simulación de intentos predefinidos
simulacion = [10, 50, 75, 85, 95, 100]
adivina_el_numero(simulacion)