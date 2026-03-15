from flask import Blueprint, request
from app.controller.ControlesController import ControlesController

controles_bp = Blueprint("controles", __name__)

controller = ControlesController()

@controles_bp.route("/controles", methods=["GET"])
def get_controles():
    data = controller.get_controles()
    return {"data": data}, 200

@controles_bp.route("/controles", methods=["POST"])
def crear_control():
    data = request.json
    resultado = controller.create_control(data)

    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Control creado",
        "data": resultado
    }

@controles_bp.route("/controles/<int:id>", methods = ["DELETE"])
def eliminar_control(id):
    resultado = controller.delete_control(id)

    if "error" in resultado:
        return resultado, 400
    
    return {
        "mensaje": "control eliminado con exito",
        "data": resultado
    }, 200

@controles_bp.route("/controles/<int:id>", methods=["PUT"])
def actualizar_control(id):
    data = request.json
    resultado = controller.actualizar_control(id, data)

    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "control actualizada",
        "data": resultado
    }, 200 