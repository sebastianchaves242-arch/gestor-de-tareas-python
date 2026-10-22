from ejercicios.tarea import Tarea
import json

class GestorTareas:

    def __init__(self):
        self.tareas = []
        self.siguiente_id = 1

    def crear_tarea(self, nombre, desc):
        if nombre.strip() == "":
            return "No puede ingresar una tarea vacia"

        resultado = self.buscar_nombre_tarea(nombre)

        if resultado is not None:
            return "Tarea ya existente"

        tarea = Tarea(self.siguiente_id, nombre, desc)
        self.tareas.append(tarea)
        self.siguiente_id += 1
        print("Tarea ingresada correctamente")

        return self.guardar_datos()

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        for tarea in self.tareas:
            print("-------------------")
            tarea.mostrarInformacion()

    def buscar_nombre_tarea(self, nombre_buscado):
        for tarea in self.tareas:
            if tarea.nombre.lower().strip() == nombre_buscado.lower().strip():
                return tarea

        return None

    def buscar_id_tarea(self, id_buscado):
        for tarea in self.tareas:
            if tarea.id == id_buscado:
                return tarea

        return None

    def actualizar_tarea(self, id_buscado, nuevo_nombre, nueva_desc):
        tarea = self.buscar_id_tarea(id_buscado)

        if tarea is not None:
            tarea.nombre = nuevo_nombre
            tarea.desc = nueva_desc
            print("Tarea actualizada correctamente.")
            return self.guardar_datos()
        else:
            return "No se encontró la tarea."

    def eliminar_tarea(self, id_buscado):
        tarea = self.buscar_id_tarea(id_buscado)

        if tarea is not None:
            self.tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
            return self.guardar_datos()
        else:
            return "No se encontró la tarea."

    def completar_tarea(self, nombre_buscado):
        tarea = self.buscar_nombre_tarea(nombre_buscado)

        if tarea is not None:
            if not tarea.completado:
                tarea.marcarCompletado()
                self.guardar_datos()
                print("Tarea marcada como completada.")
            else:
                print("La tarea ya está completada.")
        else:
            print("No se encontró la tarea.")

    def resumir_tareas(self):
        total_tareas = len(self.tareas)
        contador_completadas = 0
        contador_pendientes = 0
        for tarea in self.tareas:
            if tarea.completado:
                contador_completadas += 1
            else:
                contador_pendientes += 1

        print(f"Total de tareas: {total_tareas}")
        print(f"Tareas completadas: {contador_completadas}")
        print(f"Tareas pendientes: {contador_pendientes}")
    
    def guardar_datos(self):
        datos = []
        ids_guardados = []
    
        for tarea in self.tareas:
            if tarea.id in ids_guardados:
                return "IDs duplicados"
    
            ids_guardados.append(tarea.id)
    
            diccionario = tarea.convertirDiccionario()
            datos.append(diccionario)
    
        with open("tareas.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent = 4)
            
                

