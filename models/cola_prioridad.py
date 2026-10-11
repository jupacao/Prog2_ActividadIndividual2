# Actividad Individual 2 - Consultorio Odontológico
# Desarrollado por: Juan Pablo Castro Ocampo
# Universidad de Manizales
# Programación 2

import heapq

class ColaPrioridad:
    def __init__(self):
        self.heap = []
        self.consecutivo = 0

    def encolar(self, cita):
        peso = 1 if cita.prioridad == "Urgente" else 2
        
        heapq.heappush(self.heap, (peso, self.consecutivo, cita))
        self.consecutivo += 1

    def desencolar(self):
        if not self.esta_vacia():
            # Extraemos la tupla (peso, consecutivo, objeto_cita) y retornamos solo el objeto [índice 2]
            return heapq.heappop(self.heap)[2]
        return None

    def esta_vacia(self):
        return len(self.heap) == 0