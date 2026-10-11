# Actividad Individual 2 - Consultorio Odontológico
# Desarrollado por: Juan Pablo Castro Ocampo
# Universidad de Manizales
# Programación 2

class PilaContingencia:
    def __init__(self):
        self.items = []

    def apilar(self, cita):
        self.items.append(cita)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0