from flask import Blueprint, request
from app.controller.TerrenosController import TerrenosController

terrenos_bp = Blueprint("terrenos", __name__)
controller = TerrenosController()

@terrenos_bp.route("/terrenos", methods=["POST"])
def crear_terreno():
    data = request.json
    resultado = controller.crear_terreno(data)
    
    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Terreno creado",
        "data": resultado
    }

@terrenos_bp.route("/terrenos", methods=["GET"])
def obtener_terrenos():
    terrenos = controller.get_terrenos()
    return {
        "data": terrenos
    }

@terrenos_bp.route("/terrenos/<int:id>", methods=["DELETE"])
def eliminar_terreno(id):
    resultado = controller.delete_terreno(id)
    if "error" in resultado:
        return resultado, 400
        
    return {
        "mensaje":"Salida a terreno eliminada",
        "data":resultado
    }

@terrenos_bp.route("/terrenos/<int:id>", methods=["PUT"])
def actualizar_terreno(id):

    data = request.json
    resultado = controller.update_terreno(id, data)

    if "error" in resultado:
        return resultado, 400

    return {
        "mensaje": "Terreno actualizado",
        "data": resultado
    }, 200