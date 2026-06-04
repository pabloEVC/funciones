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

def mostrar_productos(productos):
    if not productos:
        print("El inventario está vacío.")
        return
    for nombre, (stock, precio) in productos.items():
        print(f"Producto: {nombre}, Stock: {stock}, Precio: {precio}")

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