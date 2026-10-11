# Actividad Individual 2 - Consultorio Odontológico
# Desarrollado por: Juan Pablo Castro Ocampo
# Universidad de Manizales
# Programación 2

from datetime import datetime
import holidays
from models.cola_prioridad import ColaPrioridad
from models.cola_atencion import ColaAtencion

class CitaOdontologica:
    def __init__(self, cedula, nombre, apellido, edad, telefono, tipo_cliente, tipo_atencion, prioridad, fecha_cita, hora_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        
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
        print(f"Ya se tienen datos del paciente: {paciente_previo.nombre} {paciente_previo.apellido} (Edad: {paciente_previo.edad})")
        nombre = paciente_previo.nombre
        apellido = paciente_previo.apellido
        edad = paciente_previo.edad

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
                print("Error: Seleccione una opción válida.")
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
            edad = input("Edad: ")
            if edad.isdigit() and 0 <= int(edad) <= 120:
                break
            print("Error: Ingrese una edad válida (número).")
        
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
            print("Error: Seleccione una opción válida.")

    print("Tipo de Atención (1 - Limpieza, 2 - Calzas, 3 - Extracción, 4 - Diagnóstico)")
    tipos_a = {"1": "Limpieza", "2": "Calzas", "3": "Extracción", "4": "Diagnóstico"}
    while True:
        opcion_a = input("Seleccione la opción: ")
        if opcion_a in tipos_a:
            tipo_atencion = tipos_a[opcion_a]
            break
        print("Error: Seleccione una opción válida.")
        
    print("Prioridad de Atención (1 - Normal, 2 - Urgente)")
    tipos_p = {"1": "Normal", "2": "Urgente"}
    while True:
        opcion_p = input("Seleccione la opción: ")
        if opcion_p in tipos_p:
            prioridad = tipos_p[opcion_p]
            break
        print("Error: Seleccione una opción válida.")

    fecha_actual = datetime.now().date()
    festivos_colombia = holidays.CO(language='es') 
    while True:
        fecha_cita = input("Fecha de la cita (DD/MM/AAAA): ")
        try:
            fecha_obj = datetime.strptime(fecha_cita, "%d/%m/%Y").date()
            if fecha_obj < fecha_actual:
                print("Error: La fecha de la cita no puede ser en el pasado.")
                continue
            elif fecha_obj.weekday() == 6:
                print("Error: El consultorio no atiende los domingos.")
                continue
            elif fecha_obj in festivos_colombia:
                nombre_festivo = festivos_colombia.get(fecha_obj)
                print(f"Error: Festivo nacional ({nombre_festivo}). Seleccione otro día.")
                continue
        except ValueError:
            print("Error: Ingrese una fecha válida (DD/MM/AAAA).")
            continue
            
        hora_cita = input("Hora de la cita (Formato 24h, ej. 14:30): ")
        try:
            datetime.strptime(hora_cita, "%H:%M")
        except ValueError:
            print("Error: Formato de hora inválido. Use HH:MM.")
            continue
            
        colision = False
        for p in lista_pacientes:
            if p.fecha_cita == fecha_cita and p.hora_cita == hora_cita:
                print(f">> ALERTA: Ya existe un paciente agendado el {fecha_cita} a las {hora_cita}.")
                print(">> Por favor, seleccione otro horario.")
                colision = True
                break
                
        if not colision:
            break

    return CitaOdontologica(cedula, nombre, apellido, edad, telefono, tipo_cliente, tipo_atencion, prioridad, fecha_cita, hora_cita)

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
            print("Error: Escriba 'S' o 'N'.")

    print("\n" + "="*65)
    print("INFORME 1: Agenda diaria")
    print("Atención de todos los pacientes en estricto orden de agenda")
    print("="*65)
    
    cola_agenda = ColaAtencion()
    
    for paciente in lista_pacientes:
        cola_agenda.encolar(paciente)
        
    turno_general = 1
    while not cola_agenda.esta_vacia():
        paciente_actual = cola_agenda.desencolar()
        print(f"Turno General #{turno_general}: {paciente_actual.nombre} {paciente_actual.apellido}")
        print(f"  Tratamiento: {paciente_actual.tipo_atencion} | Fecha: {paciente_actual.fecha_cita} | Hora: {paciente_actual.hora_cita}")
        turno_general += 1

    print("\n" + "="*65)
    print("INFORME 2: Plan de contingencia (Extracciones urgentes)")
    print("Filtro: Solo Extracciones + Urgentes")
    print("Orden: 1° Fecha, 2° Población Vulnerable, 3° Llegada")
    print("="*65)
    
    triage = ColaPrioridad()
    
    pacientes_filtrados = [p for p in lista_pacientes if p.tipo_atencion == "Extracción" and p.prioridad == "Urgente"]
    
    for paciente in pacientes_filtrados:
        triage.encolar(paciente)
        
    if triage.esta_vacia():
         print("No hay pacientes urgentes para extracción en este momento.")
    else:
        turno_urgencia = 1
        while not triage.esta_vacia():
            paciente_actual = triage.desencolar()
            
            edad = int(paciente_actual.edad)
            etiqueta_demo = "[⚠️ VULNERABLE]" if edad >= 65 or edad <= 12 else "[👤 ESTÁNDAR]"
            
            print(f"Llamado #{turno_urgencia} [🔴 URGENCIA] {etiqueta_demo} : {paciente_actual.nombre} {paciente_actual.apellido}")
            print(f"  Cédula: {paciente_actual.cedula}")
            print(f"  Edad: ({edad} años)")
            print(f"  Asignación: {paciente_actual.fecha_cita} a las {paciente_actual.hora_cita}")
            print("-" * 65)
            turno_urgencia += 1

if __name__ == "__main__":
    main()