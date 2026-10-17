from ejercicios.tarea import Tarea


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

        return "Tarea ingresada correctamente"

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
        else:
            print("No se encontró la tarea.")

    def eliminar_tarea(self, id_buscado):
        tarea = self.buscar_id_tarea(id_buscado)

        if tarea is not None:
            self.tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
        else:
            print("No se encontró la tarea.")

    def completar_tarea(self, nombre_buscado):
        tarea = self.buscar_nombre_tarea(nombre_buscado)

        if tarea is not None:
            if not tarea.completado:
                tarea.marcarCompletado()
                print("Tarea marcada como completada.")
            else:
                print("La tarea ya está completada.")
        else:
            print("No se encontró la tarea.")
