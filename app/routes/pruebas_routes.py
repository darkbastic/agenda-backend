from flask import Blueprint, request
from app.controller.PruebasController import PruebasController

pruebas_bp = Blueprint("pruebas", __name__)

controller = PruebasController()

@pruebas_bp.route("/pruebas",  methods=["GET"])
def obtener_pruebas():
    pruebas = controller.get_pruebas()
    return {
        "data": pruebas
    }

@pruebas_bp.route("/pruebas", methods=["POST"])
def crear_prueba():
    data = request.json
    resultado = controller.create_prueba(data)

    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Prueba creada",
        "data": resultado
    }   

@pruebas_bp.route("/pruebas/<int:id>", methods=["PUT"])
def actualizar_prueba(id):
    data = request.json
    resultado = controller.update_prueba(id, data)

    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Prueba actualizada",
        "data": resultado
    }, 200    
    
@pruebas_bp.route("/pruebas/<int:id>", methods=["DELETE"])
def eliminar_prueba(id):
    resultado = controller.delete_prueba(id)
    
    if "error" in resultado:
        return resultado, 404
    return {
        "mensaje": "Prueba eliminada",
        "data": resultado
    }, 200
