import re
from flask import request, jsonify
from src.models.user_model import UserModel

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

class UserController:
    @staticmethod
    def get_all():
        users = UserModel.get_all()
        return jsonify({
            "status": "sucesso",
            "dados": users
        }), 200

    @staticmethod
    def get_by_id(user_id):
        user = UserModel.get_by_id(user_id)
        if not user:
            return jsonify({
                "status": "erro",
                "mensagem": f"Usuário com ID '{user_id}' não foi encontrado."
            }), 404

        return jsonify({
            "status": "sucesso",
            "dados": user
        }), 200

    @staticmethod
    def create():
        data = request.get_json(silent=True)

        if data is None:
            return jsonify({
                "status": "erro",
                "mensagem": "Requisição inválida. Envie um corpo JSON no formato adequado."
            }), 400

        nome = data.get("nome")
        email = data.get("email")

        if not nome or not isinstance(nome, str) or not nome.strip():
            return jsonify({
                "status": "erro",
                "mensagem": "O campo 'nome' é obrigatório e deve ser um texto preenchido."
            }), 400

        if not email or not isinstance(email, str) or not email.strip():
            return jsonify({
                "status": "erro",
                "mensagem": "O campo 'email' é obrigatório e deve ser um texto preenchido."
            }), 400

        if not re.match(EMAIL_REGEX, email.strip()):
            return jsonify({
                "status": "erro",
                "mensagem": "O campo 'email' informado possui um formato inválido."
            }), 400

        sanitized_data = {
            "nome": nome.strip(),
            "email": email.strip().lower(),
            "cargo": data.get("cargo", "").strip() if isinstance(data.get("cargo"), str) else ""
        }

        new_user = UserModel.create(sanitized_data)
        return jsonify({
            "status": "sucesso",
            "mensagem": "Usuário cadastrado com sucesso.",
            "dados": new_user
        }), 201

    @staticmethod
    def update(user_id):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({
                "status": "erro",
                "mensagem": "Corpo da requisição vazio. Forneça os dados para atualização."
            }), 400

        updated_user = UserModel.update(user_id, data)
        if not updated_user:
            return jsonify({
                "status": "erro",
                "mensagem": f"Usuário com ID '{user_id}' não foi encontrado para atualização."
            }), 404

        return jsonify({
            "status": "sucesso",
            "mensagem": "Usuário atualizado com sucesso.",
            "dados": updated_user
        }), 200

    @staticmethod
    def delete(user_id):
        success = UserModel.delete(user_id)
        if not success:
            return jsonify({
                "status": "erro",
                "mensagem": f"Usuário com ID '{user_id}' não foi encontrado para remoção."
            }), 404

        return jsonify({
            "status": "sucesso",
            "mensagem": f"Usuário com ID '{user_id}' foi removido com sucesso."
        }), 200
