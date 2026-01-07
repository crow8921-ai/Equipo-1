import json
import os
from datetime import datetime

class GestorInventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = self._cargar_datos()

    def _cargar_datos(self):
        
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def guardar(self):
        
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f" Error al guardar: {e}")

    def agregar_producto(self):
        print("\n--- Registrar Nuevo Producto ---")
        try:
            nombre = input("Nombre: ").strip().capitalize()
            cantidad = int(input("Cantidad inicial: "))
            precio = float(input("Precio unitario: "))
            
            if cantidad < 0 or precio < 0:
                raise ValueError("No se permiten valores negativos.")

            self.productos.append({
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio,
                "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            self.guardar()
            print(f"'{nombre}' añadido exitosamente.")
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    def listar_inventario(self):
        if not self.productos:
            print("\n El inventario está vacío.")
            return

        print(f"\n{'ID':<4} | {'Producto':<20} | {'Stock':<8} | {'Precio':<10}")
        print("-" * 50)
        for idx, p in enumerate(self.productos):
            print(f"{idx:<4} | {p['nombre']:<20} | {p['cantidad']:<8} | ${p['precio']:<10.2f}")

    def actualizar_stock(self):
        self.listar_inventario()
        try:
            idx = int(input("\nID del producto a modificar: "))
            p = self.productos[idx]
            
            print(f"Editando: {p['nombre']}")
            p['cantidad'] = int(input(f"Nueva cantidad (actual {p['cantidad']}): "))
            p['precio'] = float(input(f"Nuevo precio (actual {p['precio']}): "))
            
            self.guardar()
            print(" Actualización completada.")
        except (IndexError, ValueError):
            print(" ID o valor inválido.")

    def eliminar_producto(self):
        self.listar_inventario()
        try:
            idx = int(input("\nID del producto a eliminar: "))
            eliminado = self.productos.pop(idx)
            self.guardar()
            print(f" Se eliminó '{eliminado['nombre']}' del sistema.")
        except (IndexError, ValueError):
            print(" No se pudo eliminar el producto.")

def main():
    sistema = GestorInventario()
    
    menu = """
    ╔════════════════════════════════╗
    ║      BODEX SYSTEM PRO v2.0     ║
    ╠════════════════════════════════╣
    ║ 1. Ver Inventario              ║
    ║ 2. Agregar Producto            ║
    ║ 3. Actualizar Stock/Precio     ║
    ║ 4. Eliminar Producto           ║
    ║ 5. Salir                       ║
    ╚════════════════════════════════╝
    """
    
    while True:
        print(menu)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sistema.listar_inventario()
        elif opcion == "2":
            sistema.agregar_producto()
        elif opcion == "3":
            sistema.actualizar_stock()
        elif opcion == "4":
            sistema.eliminar_producto()
        elif opcion == "5":
            print("Cerrando sistema... ¡Hasta pronto!")
            break
        else:
            print(" Opción no reconocida.")

if __name__ == "__main__":
    main()