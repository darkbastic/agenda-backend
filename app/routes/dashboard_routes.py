from flask import Blueprint
from app.controller.dashboard_controller import DashboardController

dashboard_bp = Blueprint("dashboard", __name__)
controller = DashboardController()

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():

    data = controller.get_dashboard()

    return {
        "data": data
    }, 200