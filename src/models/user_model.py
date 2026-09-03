import uuid

users_db = []

class UserModel:
    @staticmethod
    def get_all():
        return users_db

    @staticmethod
    def get_by_id(user_id):
        return next((user for user in users_db if user["id"] == user_id), None)

    @staticmethod
    def create(data):
        new_user = {
            "id": str(uuid.uuid4()),
            "nome": data.get("nome"),
            "email": data.get("email"),
            "cargo": data.get("cargo", "")
        }
        users_db.append(new_user)
        return new_user

    @staticmethod
    def update(user_id, data):
        user = UserModel.get_by_id(user_id)
        if not user:
            return None
        
        user["nome"] = data.get("nome", user["nome"])
        user["email"] = data.get("email", user["email"])
        user["cargo"] = data.get("cargo", user["cargo"])
        return user

    @staticmethod
    def delete(user_id):
        global users_db
        user = UserModel.get_by_id(user_id)
        if not user:
            return False
        
        users_db = [u for u in users_db if u["id"] != user_id]
        return True
