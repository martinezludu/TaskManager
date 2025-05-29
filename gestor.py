class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✔️" if self.completada else "⏳"
        return f"{self.titulo} - {estado}"


def mostrar_menu_tareas():
    tareas = []
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Volver al menú principal")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            titulo = input("Ingrese el nombre de la tarea: ").lower()
            t1 = Tarea(titulo)
            tareas.append(t1)
            print("✅ Tarea agregada.")

        elif opcion == "2":
            if not tareas:
                print("⚠️ No hay tareas cargadas.")
            else:
                print("\n📋 Lista de tareas:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}.{tarea}")
                    
        elif opcion == "3":
            if not tareas:
                print("⚠️ No hay tareas cargadas.")
            else:
                print("\n📋 Lista de tareas:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}.{tarea}")
                    
                try:
                    indice= int(input("¡Que numero de tarea queres marcar como completada?"))
                    if 1<= indice <= len(tareas):
                            tareas[indice -1].marcar_completada()
                            print("✅ Tarea marcada como completada.")
                    else:
                        print("❌ Número inválido.")
                except ValueError:
                    print("❌ Ingresá un número válido.")
        elif opcion == "4":
            if not tareas:
                print("⚠️ No hay tareas para eliminar.")
            else:
                try:
                    indice = int(input("¿Qué número de tarea querés eliminar? "))
                    if 1 <= indice <= len(tareas):
                        tarea_eliminada = tareas.pop(indice - 1)
                        print(f"🗑️ Tarea eliminada: {tarea_eliminada.titulo}")
                    else:
                        print("❌ Número inválido.")
                except ValueError:
                    print("❌ Ingresá un número válido.")
        elif opcion == "5":
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")