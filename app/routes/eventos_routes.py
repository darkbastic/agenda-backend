from flask import Blueprint
from app.controller.EventosController import EventosController

eventos_bp = Blueprint("eventos", __name__)

controller = EventosController()

@eventos_bp.route("/eventos", methods=["GET"])
def obtener_eventos():

    eventos = controller.get_eventos()

    return {
        "data": eventos
    }, 200