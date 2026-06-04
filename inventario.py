def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre == "":
        print("El nombre del producto no puede estar vacío.")
        return
    if nombre in productos:
        print("El producto ya existe en el inventario.")
        return
    stock = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))
    productos[nombre] = [stock, precio]
    print("Producto agregado exitosamente.")

def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    if nombre in productos:
        print(f"Producto: {nombre}, Stock: {productos[nombre][0]}, Precio: {productos[nombre][1]}")
    else:
        print("Producto no encontrado.")

def producto_mas_caro(productos):
    if not productos:
        print("El inventario está vacío.")
        return
    producto = max(productos, key=lambda x: productos[x][1])
    print(f"Producto más caro: {producto}, Precio: {productos[producto][1]}")

productos = {
    "mouse": [10, 15000],
    "teclado": [5, 30000],
    "monitor": [2, 180000]
}
while True:
    print("menu")
    while True:
        try:
            print("1. Agregar producto")
            print("2. Mostrar producto")
            print("3. Buscar productos")
            print("4. Producto mas caro")
            print("5. Salir")
            op = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
    match op:
        case 1: 
            agregar_producto(productos)
        case 2: 
            print(productos)
        case 3: 
            buscar_producto(productos)
        case 4: 
            producto_mas_caro(productos)
        case 5: 
            break
        case _: 
            print("Opcion no valida")