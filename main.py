from inventario import Inventario
from producto import Producto

inv = Inventario()

while True:
    print("\n1. Agregar")
    print("2. Mostrar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

    op = input("Opción: ")

    try:
        if op == "1":
            idp = int(input("ID: "))
            nombre = input("Nombre: ")
            cant = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar_producto(Producto(idp, nombre, cant, precio))
            input("Presione Enter para continuar...")

        elif op == "2":
            for p in inv.productos:
                print(p.id, p.nombre, p.cantidad, p.precio)
            input("Presione Enter para continuar...")

        elif op == "3":
            idp = int(input("ID: "))
            cant = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inv.actualizar_producto(idp, cant, precio)
            input("Presione Enter para continuar...")

        elif op == "4":
            idp = int(input("ID: "))
            inv.eliminar_producto(idp)
            input("Presione Enter para continuar...")

        elif op == "5":
            break

    except ValueError:
        print("Error: datos inválidos.")
        input("Presione Enter para continuar...")