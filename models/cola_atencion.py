# Actividad Individual 2 - Consultorio Odontológico
# Desarrollado por: Juan Pablo Castro Ocampo
# Universidad de Manizales
# Programación 2

from collections import deque

class ColaAtencion:
    def __init__(self):
        self.items = deque()

    def encolar(self, cita):
        self.items.append(cita)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def esta_vacia(self):
        return len(self.items) == 0