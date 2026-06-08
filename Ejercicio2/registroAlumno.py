import funcionesRegistro
alumnos ={
    "Ana": [5.5, 6.0, 48],
    "Luis": [3.9, 6.8, 7.0],
    "Pedro": [6.5, 6.8, 7.0],
}



while True:
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Mejor alumno")
    print("4. Ver promedio")
    print("5. Cantidad de reprobados")
    print("6. Salir")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    match opcion:
        case 1:
            funcionesRegistro.agregar_alumno(alumnos)
        case 2:
            funcionesRegistro.mostrar_alumnos(alumnos)
        case 3:            
            funcionesRegistro.ver_promedio(alumnos)
        case 4:            
            funcionesRegistro.mejor_alumno(alumnos)
        case 5:            
            funcionesRegistro.cantidad_reprobados(alumnos)
        case 6:            
            print("Salir")
            break