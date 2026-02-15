from producto import Producto
from inventario import Inventario

inventario = Inventario()

while True:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("ID: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
        input("Presiona ENTER para continuar...")

    elif opcion == "2":
        id = input("ID del producto a eliminar: ")
        inventario.eliminar_producto(id)
        input("Presiona ENTER para continuar...")

    elif opcion == "3":
        id = input("ID del producto a actualizar: ")
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        inventario.actualizar_producto(id, cantidad, precio)
        input("Presiona ENTER para continuar...")

    elif opcion == "4":
        nombre = input("Nombre a buscar: ")
        inventario.buscar_producto(nombre)
        input("Presiona ENTER para continuar...")

    elif opcion == "5":
        inventario.mostrar_productos()
        input("Presiona ENTER para continuar...")

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
        input("Presiona ENTER para continuar...")
