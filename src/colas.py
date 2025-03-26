from collections import deque

class Cola:
    def __init__(self):
        self.cola = deque()

    def encolar(self, elemento):
        self.cola.append(elemento)
        print(f"Encolado: {elemento}")

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        return self.cola.popleft()

    def esta_vacia(self):
        return len(self.cola) == 0

    def ver_primero(self):
        return self.cola[0] if not self.esta_vacia() else None

    def mostrar_cola(self):
        print("Cola actual:", list(self.cola))

# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.mostrar_cola()

print(f"Desencolado: {cola.desencolar()}")
cola.mostrar_cola()

print(f"Primer elemento: {cola.ver_primero()}")
