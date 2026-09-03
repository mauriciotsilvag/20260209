from flask import Flask, jsonify
from src.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    
    # Registro de Blueprints (Rotas)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    
    # Rota Health Check
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({
            "status": "sucesso",
            "mensagem": "API Connect executando com sucesso!"
        }), 200
        
    return app
