import json
import os

class BodexBackend:
    def __init__(self, archivo="almacen.json"):
        self.archivo = archivo
        self.datos = self.cargar()

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"productos": []}

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4)

    def agregar(self):
        nombre = input("Nombre del producto: ")
        stock = int(input("Stock inicial: "))
        precio = float(input("Precio: "))
        self.datos["productos"].append({"nombre": nombre, "stock": stock, "precio": precio})
        self.guardar()
        print("Producto agregado.")

    def eliminar(self):
        nombre = input("Nombre del producto a eliminar: ").lower()
        original = len(self.datos["productos"])
        self.datos["productos"] = [p for p in self.datos["productos"] if p['nombre'].lower() != nombre]
        
        if len(self.datos["productos"]) < original:
            self.guardar()
            print("Producto eliminado del catálogo.")
        else:
            print(" No se encontró el producto.")

    def mostrar(self):
        print("\n--- INVENTARIO ACTUAL ---")
        for p in self.datos["productos"]:
            status = "DISPONIBLE" if p['stock'] > 0 else "AGOTADO"
            print(f"[{status}] {p['nombre']} | Stock: {p['stock']} | Precio: ${p['precio']}")

def menu():
    app = BodexBackend()
    while True:
        print("\n1. Ver | 2. Agregar | 3. Eliminar | 4. Salir")
        op = input("Seleccione: ")
        if op == "1": app.mostrar()
        elif op == "2": app.agregar()
        elif op == "3": app.eliminar()
        elif op == "4": break

if __name__ == "__main__":
    menu()