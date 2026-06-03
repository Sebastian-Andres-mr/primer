tareas ={
    "hogar":[],
    "trabajo":[],
    "estudio":[]
    
}
print("Prueba para subir al github")
print("Prueba para subir al github")
print("Prueba para subir al github")
print("Prueba para subir al github")
print("Prueba para subir al github")
print("Prueba para subir al github")
while True:
    print("---Gestión de tareas---")
    print("1- Hogar")
    print("2- Trabajo")
    print("3- Estudio")
    print("4- Listar tareas")
    print("5- Salir")
    op = input("selecciones una opción: ")
    if op in "12345":
        if op in "123":
            tarea = input("Ingrese la tarea: ")
    match op:
        case "1":
            tareas["hogar"].append(tarea)
        case "2":
            tareas["trabajo"].append(tarea)
        case "3":
            tareas["Estudio"].append(tarea)
        case "4":
            print("---Detalle de Tareas---")
            print(f"Hogar - {len(tareas["hogar"])}")
            for tarea in tareas["hogar"]:
                print(f"  -{tarea}")
            print(f"Trabajo - {len(tareas["Trabajo"])}")
            for tarea in tareas["Trabajo"]:
                print(f"  -{tarea}")
            print(f"Estudio - {len(tareas["Estudio"])}")
            for tarea in tareas["Estudio"]:
                print(f"  -{tarea}")
        case "5":
                print("chaito")
                break