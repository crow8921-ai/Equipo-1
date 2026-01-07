from flask import Flask, render_template, request, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)
DB = "inventario.json"

def cargar():
    if os.path.exists(DB):
        with open(DB, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar(data):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/productos", methods=["GET"])
def obtener_productos():
    return jsonify(cargar())

@app.route("/api/productos", methods=["POST"])
def agregar_producto():
    productos = cargar()
    p = request.json
    p["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    productos.append(p)
    guardar(productos)
    return jsonify({"ok": True})

@app.route("/api/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    productos = cargar()
    productos = [p for p in productos if p["id"] != id]
    guardar(productos)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)