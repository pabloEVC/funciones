
from funcionesInventario import agregar_producto, mostrar_productos, buscar_producto, producto_mas_caro
productos = {}
productos = {
    "mouse": [10, 15000],
    "teclado": [5, 30000],
    "monitor": [2, 180000]
}
while True:
    print("menu")
    
        
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar productos")
    print("4. Producto mas caro")
    print("5. Salir")
    op = int(input("Ingrese una opcion: "))
    

    print("Por favor, ingrese un número válido.")
        
    match op:
        case 1: 
            agregar_producto(productos)
        case 2: 
            mostrar_productos(productos)
        case 3: 
            buscar_producto(productos)
        case 4: 
            producto_mas_caro(productos)
        case 5: 
            break
        case _: 
            print("Opcion no valida")