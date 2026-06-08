def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    alumnos[nombre] = notas
def mostrar_alumnos(alumnos):
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {notas}")

def ver_promedio(alumnos):
    """calcula el promedio de cada alumno y lo muestra"""
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")
def mejor_alumno(alumnos):
    """calcula el promedio de cada alumno y muestra el mejor"""
    mejor_promedio = 0
    mejor_alumno = ""
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = nombre
    print(f"El mejor alumno es {mejor_alumno} con un promedio de {mejor_promedio:.2f}")
def cantidad_reprobados(alumnos):
    """cuenta la cantidad de alumnos que tienen un promedio menor a 6"""
    reprobados = 0
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        if promedio < 4:
            reprobados += 1
    print(f"Cantidad de alumnos reprobados: {reprobados}")