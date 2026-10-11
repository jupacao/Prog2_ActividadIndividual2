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
        fecha_orden = cita.obtener_fecha_obj()
        
        edad = int(cita.edad)
        vulnerabilidad = 1 if edad >= 65 or edad <= 12 else 2
        
        heapq.heappush(self.heap, (fecha_orden, vulnerabilidad, self.consecutivo, cita))
        self.consecutivo += 1

    def desencolar(self):
        if not self.esta_vacia():
            return heapq.heappop(self.heap)[3]
        return None

    def esta_vacia(self):
        return len(self.heap) == 0