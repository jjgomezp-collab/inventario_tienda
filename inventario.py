# inventario.py
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # =========================
    # ARCHIVOS
    # =========================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("Archivo de inventario creado.")

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        idp = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])
                        self.productos.append(
                            Producto(idp, nombre, cantidad, precio)
                        )
                    else:
                        print("Línea corrupta ignorada.")

        except PermissionError:
            print("Error: sin permisos para leer el archivo.")
        except Exception as e:
            print("Error al cargar archivo:", e)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:
            print("Error: sin permisos para escribir.")
        except Exception as e:
            print("Error al guardar:", e)

    # =========================
    # OPERACIONES
    # =========================
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado y guardado.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        for p in self.productos:
            if p.id == id_producto:
                p.cantidad = cantidad
                p.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")