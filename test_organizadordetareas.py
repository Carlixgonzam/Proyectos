tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Tarea '{task}' agregada.")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Tarea '{task}' eliminada.")
    else:
        print(f"Tarea '{task}' no encontrada.")


def list_tasks():
    if tasks:
        print("Tareas:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No hay tareas disponibles.")


def main():
    while True:
        print("\Opciones:")
        print("1. Agregar tarea")
        print("2. Remover tarea")
        print("3. Lista de tareas")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            task = input("Insertar tarea: ")
            add_task(task)
        elif choice == "2":
            task = input("Insertar tarea para eliminar: ")
            remove_task(task)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
