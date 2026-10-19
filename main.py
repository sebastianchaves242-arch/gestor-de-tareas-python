
from ejercicios.gestor_tareas import GestorTareas


def main():
    gestor = GestorTareas()

    while True:
        print("\n===== GESTOR DE TAREAS =====")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Buscar tarea")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Completar tarea")
        print("7. Resumir tareas")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            desc = input("Descripción: ")
            gestor.crear_tarea(nombre, desc)

        elif opcion == "2":
            gestor.listar_tareas()

        elif opcion == "3":
            nombre = input("Nombre de la tarea: ")
            tarea = gestor.buscar_nombre_tarea(nombre)

            if tarea is not None:
                tarea.mostrarInformacion()
            else:
                print("No se encontró ninguna tarea.")

        elif opcion == "4":
            id_tarea = int(input("ID de la tarea: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_desc = input("Nueva descripción: ")

            gestor.actualizar_tarea(
                id_tarea, nuevo_nombre, nueva_desc
            )

        elif opcion == "5":
            id_tarea = int(input("ID de la tarea: "))
            gestor.eliminar_tarea(id_tarea)

        elif opcion == "6":
            nombre = input("Nombre de la tarea: ")
            gestor.completar_tarea(nombre)

        elif opcion == "7":
            gestor.resumir_tareas()
        
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
