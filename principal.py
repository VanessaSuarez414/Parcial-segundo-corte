from productos import catalogo, Producto
from factura import Factura

# Mostrar catálogo por categoría
def mostrar_catalogo():
    print("\nCATÁLOGO DE PRODUCTOS")
    for categoria, productos in catalogo.items():
        print(f"\n{categoria}:")
        for codigo, producto in productos.items():
            print(f"  {codigo} - {producto.nombre} (${producto.precio:,})")
# Buscar producto por código (en cualquier categoría)
def buscar_producto(codigo):
    for productos in catalogo.values():
        if codigo in productos:
            return productos[codigo]
    return None
# Agregar un nuevo producto al catálogo
def agregar_producto_catalogo():
    print("\nAGREGAR NUEVO PRODUCTO")
    print("Categorías disponibles:")
    for i, categoria in enumerate(catalogo.keys(), start=1):
        print(f"{i}. {categoria}", end="\n")
    try:
        opcion = int(input("Seleccione la categoría (número): "))
        categoria = list(catalogo.keys())[opcion - 1]
    except (ValueError, IndexError):
        print("Opción no válida.")
        return
    codigo = input("Ingrese código del producto (por ejemplo PE006): ").upper()
    nombre = input("Ingrese nombre del producto: ")
    try:
        precio = int(input("Ingrese precio del producto: "))
    except ValueError:
        print("Precio inválido.")
        return
    # Crear nuevo producto y agregarlo al diccionario
    nuevo_producto = Producto(codigo, nombre, precio, categoria)
    catalogo[categoria][codigo] = nuevo_producto
    print(f"Producto '{nombre}' agregado a la categoría '{categoria}'.\n")
# Agregar una nueva categoría al catálogo
def agregar_categoria():
    print("\nAGREGAR NUEVA CATEGORÍA")
    nueva_categoria = input("Ingrese el nombre de la nueva categoría: ")
    if nueva_categoria in catalogo:
        print("La categoría ya existe.")
    else:
        catalogo[nueva_categoria] = {}
        print(f"Categoría '{nueva_categoria}' agregada al catálogo.\n")
# Ver facturas guardadas en un archivo
def ver_facturas_guardadas():
    print("\nFACTURAS GUARDADAS")
    try:
        with open("facturas.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print(contenido)
            else:
                print("No hay facturas guardadas.")
    except FileNotFoundError:
        print("No se encontró el archivo de facturas.")
# Programa principal
def main():
    print("Bienvenido al sistema de facturación de ElectroMundo S.A.")
    cliente = input("Ingrese el nombre del cliente: ")
    factura = Factura(cliente)
    while True:
        print("1. Mostrar catálogo")
        print("2. Agregar producto a la factura")
        print("3. Ver factura")
        print("4. Agregar nuevo producto al catálogo")
        print("5. Crear nueva categoría")
        print("6. Ver facturas guardadas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            mostrar_catalogo()
            codigo = input("Ingrese el código del producto: ").upper()
            producto = buscar_producto(codigo)
            if producto:
                try:
                    cantidad = int(input("Cantidad: "))
                    factura.agregar_producto(producto, cantidad)
                    print("Producto agregado a la factura.")
                except ValueError:
                    print("Cantidad inválida.")
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            factura.mostrar_factura()
        elif opcion == "4":
            agregar_producto_catalogo()
        elif opcion == "5":
            agregar_categoria()
        elif opcion == "6":
            ver_facturas_guardadas()
        elif opcion == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")
# Ejecución directa
if __name__ == "__main__":
    main()
