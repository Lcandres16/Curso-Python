tareas = []

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción que desee: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea que desea agregar: ")
        tareas.append(tarea)
        print("Tarea agregada con éxito.")
    elif opcion == "2":
        if tareas:
            print("Tareas pendientes:")
            for idx, tarea in enumerate(tareas, start=1):
                print(f"{idx}. {tarea}")
            try:
                idx = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
                if 0 <= idx < len(tareas):
                    tarea_eliminada = tareas.pop(idx)
                    print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
        else:
            print("No hay tareas pendientes para eliminar.")
    elif opcion == "3":
        if tareas:
            print("Tareas pendientes:")
            for idx, tarea in enumerate(tareas, start=1):
                print(f"{idx}. {tarea}")
        else:
            print("No hay tareas pendientes.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
