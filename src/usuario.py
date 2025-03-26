import random
import string

def generar_usuario(nombre, apellido):
    numero = random.randint(100, 999)
    usuario = f"{nombre.lower()}{apellido.lower()}{numero}"
    return usuario

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def crear_cuenta(nombre, apellido):
    usuario = generar_usuario(nombre, apellido)
    contraseña = generar_contraseña()
    return usuario, contraseña

# Ejemplo de uso
nombre = "Carlos"
apellido = "Pérez"
usuario, contraseña = crear_cuenta(nombre, apellido)
print(f"Usuario generado: {usuario}")
print(f"Contraseña segura: {contraseña}")