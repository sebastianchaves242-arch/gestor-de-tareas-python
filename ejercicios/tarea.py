import json

class Tarea:

    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc
        self.completado = False

    def mostrarInformacion(self):
        estado = "Completada" if self.completado else "Pendiente"

        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.desc}")
        print(f"Estado: {estado}")

    def marcarCompletado(self):
        self.completado = True

    def convertirDiccionario(self):
        tarea = {
            "id": self.id, 
            "nombre": self.nombre, 
            "descripcion": self.desc, 
            "completado": self.completado     
        }
        return tarea



