def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    alumnos[nombre] = notas
def mostrar_alumnos
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
    opcion = int(input("Seleccione una opción: "))
    match opcion:
        case 1:
            print("Agregar alumno")
        case 2:
            print("Mostrar alumnos")
        case 3:            
            print("Ver promedio")
        case 4:            
            print("Mejor alumno")
        case 5:            
            print("Cantidad de reprobados")
        case 6:            
            print("Salir")