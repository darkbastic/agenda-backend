from flask import Flask
from flask_cors import CORS
from app.routes.pruebas_routes import pruebas_bp
from app.routes.eventos_routes import eventos_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.controles_routes import controles_bp
from app.routes.terrenos_routes import terrenos_bp
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(pruebas_bp)
app.register_blueprint(eventos_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(controles_bp)
app.register_blueprint(terrenos_bp)
    
@app.route("/")
def home():
    return {"mensaje": "Servidor funcionando"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)