class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID ya existe")
                return
        self.productos.append(producto)
        print("Producto agregado")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado")
                return
        print("Producto no encontrado")

    def actualizar_producto(self, id, cantidad, precio):
        for p in self.productos:
            if p.get_id() == id:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos")

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío")
        for p in self.productos:
            print(p)
