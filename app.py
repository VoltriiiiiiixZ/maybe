from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # autorise les requêtes cross-origin

# Utilisateurs fictifs (pour test)
users = {
    "entrepriseX": "voici",
    "Diego": "1999",
    "Aaron": "1999",
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify(success=True, message="Connexion réussie !")
    else:
        return jsonify(success=False, message="Identifiants invalides"), 401
