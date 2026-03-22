from flask import Blueprint, request
from app.controller.EstudioController import EstudioController

estudio_bp = Blueprint("estudio", __name__)
controller = EstudioController()

@estudio_bp.route("/estudio", methods=["POST"])
def crear_estudio():
    data = request.json
    resultado = controller.crear_estudio(data)
    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Estudio creado",
        "data": resultado
    }

@estudio_bp.route("/estudio", methods=["GET"])
def obtener_estudios():
    estudios = controller.get_estudios()
    return {
        "data": estudios
    },200

@estudio_bp.route("/estudio/semana", methods=["GET"])
def obtener_estudios_semana():
    fecha_inicio = request.args.get("fecha_inicio")
    estudios = controller.get_estudios_semana(fecha_inicio)

    if "error" in estudios:
        return estudios, 400 
    return {
        "data": estudios
    },200

@estudio_bp.route("/estudio/<int:id>", methods=["PUT"])
def actualizar_estudio(id):
    data = request.json

    resultado = controller.update_estudio(id, data)

    if "error" in resultado:
        return resultado, 400

    return {
        "mensaje": "Estudio actualizado",
        "data": resultado
    }, 200

@estudio_bp.route("/estudio/<int:id>", methods=["DELETE"])
def eliminar_estudio(id):
    resultado = controller.eliminar_estudio(id)

    if "error" in resultado:
        return resultado, 400
    return {
        "mensaje": "Estudio eliminado",
        "data": resultado
    }, 200

@estudio_bp.route("/estudio/estado/<int:id>", methods=["PUT"])
def cambiar_estado(id):
    resultado = controller.updated_estado(id)
    if "error" in resultado:
        return resultado, 400
    return{
        "mensaje": "estado modificado",
        "data": resultado
    }, 200