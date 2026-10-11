# Actividad Individual 2 - Consultorio Odontológico
# Desarrollado por: Juan Pablo Castro Ocampo
# Universidad de Manizales
# Programación 2

from datetime import datetime
import holidays
from models.cola_prioridad import ColaPrioridad

class CitaOdontologica:
    def __init__(self, cedula, nombre, apellido, telefono, tipo_cliente, tipo_atencion, prioridad, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        
    def obtener_fecha_obj(self):
        return datetime.strptime(self.fecha_cita, "%d/%m/%Y").date()

def es_invalido_por_patron(cadena):
    if len(set(cadena)) == 1:
        return True
    es_ascendente = all(int(cadena[i]) == int(cadena[i-1]) + 1 for i in range(1, len(cadena)))
    es_descendente = all(int(cadena[i]) == int(cadena[i-1]) - 1 for i in range(1, len(cadena)))
    return es_ascendente or es_descendente

def capturar_datos(lista_pacientes):
    print("\n--- INGRESO DE DATOS DEL PACIENTE ---")
    while True:
        cedula = input("Cédula: ")
        if not (cedula.isdigit() and 7 <= len(cedula) <= 10):
            print("Error: Verifique la cédula.")
        elif es_invalido_por_patron(cedula):
            print("Error: Verifique la cédula.")
        else:
            break

    paciente_previo = None
    for cita in lista_pacientes:
        if cita.cedula == cedula:
            paciente_previo = cita
            break

    if paciente_previo:
        print(f"Ya se tienen datos del paciente: {paciente_previo.nombre} {paciente_previo.apellido}")
        nombre = paciente_previo.nombre
        apellido = paciente_previo.apellido

        while True:
            cambiar_tel = input(f"Teléfono actual: {paciente_previo.telefono} ¿Desea actualizarlo? (S/N): ").lower()
            if cambiar_tel in ['s', 'n']:
                break
            print("Error: Escriba 'S' para Sí o 'N' para No.")
            
        if cambiar_tel == 's':
            while True:
                telefono = input("Ingrese el nuevo teléfono: ")
                if not (telefono.isdigit() and len(telefono) == 10):
                    print("Error: Verifique el teléfono, debe ser de 10 dígitos.")
                elif not telefono.startswith(('3', '6')):
                    print("Error: Verifique el teléfono, debe iniciar con 3 (Celular) o 6 (Fijo).")
                elif es_invalido_por_patron(telefono):
                    print("Error: Verifique el teléfono.")
                else:
                    break
        else:
            telefono = paciente_previo.telefono
            
        while True:
            cambiar_tipo = input(f"Tipo de plan actual: {paciente_previo.tipo_cliente} ¿Desea actualizarlo? (S/N): ").lower()
            if cambiar_tipo in ['s', 'n']:
                break
            print("Error: Escriba 'S' para Sí o 'N' para No.")
            
        if cambiar_tipo == 's':
            print("Ingrese el nuevo tipo de cliente (1 - Particular, 2 - EPS, 3 - Prepagada)")
            tipos_c = {"1": "Particular", "2": "EPS", "3": "Prepagada"}
            while True:
                opcion_c = input("Seleccione la opción: ")
                if opcion_c in tipos_c:
                    tipo_cliente = tipos_c[opcion_c]
                    break
                print("Error: Seleccione una opción válida (1 - Particular, 2 - EPS, 3 - Prepagada).")
        else:
            tipo_cliente = paciente_previo.tipo_cliente
            
    else: 
        while True:
            nombre = input("Nombre: ")
            if nombre.replace(" ", "").isalpha():
                break
            print("Error: El nombre no puede contener números.")
        
        while True:
            apellido = input("Apellido: ")
            if apellido.replace(" ", "").isalpha():
                break
            print("Error: El apellido no puede contener números.")
        
        while True:
            telefono = input("Teléfono: ")
            if not (telefono.isdigit() and len(telefono) == 10):
                print("Error: Verifique el teléfono, debe ser de 10 dígitos.")
            elif not telefono.startswith(('3', '6')):
                print("Error: Verifique el teléfono, debe iniciar con 3 (Celular) o 6 (Fijo).")
            elif es_invalido_por_patron(telefono):
                print("Error: Verifique el teléfono.")
            else:
                break

        print("Tipo de cliente (1 - Particular, 2 - EPS, 3 - Prepagada)")
        tipos_c = {"1": "Particular", "2": "EPS", "3": "Prepagada"}
        while True:
            opcion_c = input("Seleccione la opción: ")
            if opcion_c in tipos_c:
                tipo_cliente = tipos_c[opcion_c]
                break
            print("Error: Seleccione una opción válida (1 - Particular, 2 - EPS, 3 - Prepagada).")

    print("Tipo de Atención (1 - Limpieza, 2 - Calzas, 3 - Extracción, 4 - Diagnóstico)")
    tipos_a = {"1": "Limpieza", "2": "Calzas", "3": "Extracción", "4": "Diagnóstico"}
    while True:
        opcion_a = input("Seleccione la opción: ")
        if opcion_a in tipos_a:
            tipo_atencion = tipos_a[opcion_a]
            break
        print("Error: Seleccione una opción válida (1 - Limpieza, 2 - Calzas, 3 - Extracción, 4 - Diagnóstico).")
        
    print("Prioridad de Atención (1 - Normal, 2 - Urgente)")
    tipos_p = {"1": "Normal", "2": "Urgente"}
    while True:
        opcion_p = input("Seleccione la opción: ")
        if opcion_p in tipos_p:
            prioridad = tipos_p[opcion_p]
            break
        print("Error: Seleccione una opción válida (1 - Normal, 2 - Urgente).")

    fecha_actual = datetime.now().date()
    festivos_colombia = holidays.CO(language='es') 
    while True:
        fecha_cita = input("Fecha de la cita (DD/MM/AAAA): ")
        try:
            fecha_obj = datetime.strptime(fecha_cita, "%d/%m/%Y").date()
            if fecha_obj < fecha_actual:
                print("Error: La fecha de la cita no puede ser anterior al día de hoy.")
            elif fecha_obj.weekday() == 6:
                print("Error: El consultorio no atiende los domingos. Por favor seleccione otro día.")
            elif fecha_obj in festivos_colombia:
                nombre_festivo = festivos_colombia.get(fecha_obj)
                print(f"Error: El consultorio no atiende en días festivos ({nombre_festivo}). Por favor seleccione otro día.")
            else:
                break
        except ValueError:
            print("Error: Ingrese una fecha válida usando el formato DD/MM/AAAA.")

    return CitaOdontologica(cedula, nombre, apellido, telefono, tipo_cliente, tipo_atencion, prioridad, fecha_cita)

def main():
    lista_pacientes = []
    continuar = "s"
    
    while continuar.lower() == "s":
        cita = capturar_datos(lista_pacientes)
        lista_pacientes.append(cita)
        while True:
            continuar = input("\n¿Desea ingresar otro paciente? (S/N): ").lower()
            if continuar in ["s", "n"]:
                break
            print("Error: Escriba 'S' para Sí o 'N' para No.")

    print("\n" + "="*60)
    print("--- LISTA DE PACIENTES EN ORDEN DE ATENCIÓN ---")
    print("Orden: 1° Urgencias (por llegada), 2° Normales (por llegada)")
    print("="*60)
    
    triage = ColaPrioridad()
    
    for paciente in lista_pacientes:
        triage.encolar(paciente)
        
    turno = 1
    while not triage.esta_vacia():
        paciente_actual = triage.desencolar()
        
        etiqueta = "[🔴 URGENCIA]" if paciente_actual.prioridad == "Urgente" else "[🟢 NORMAL]"
        
        print(f"Llamado #{turno} {etiqueta} : {paciente_actual.nombre} {paciente_actual.apellido}")
        print(f"  Cédula: {paciente_actual.cedula}")
        print(f"  Tratamiento: {paciente_actual.tipo_atencion}")
        print(f"  Fecha asignada: {paciente_actual.fecha_cita}")
        print("-" * 60)
        turno += 1

if __name__ == "__main__":
    main()