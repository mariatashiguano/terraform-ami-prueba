from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilitamos CORS para que el Frontend (Curso B) pueda hablar con nosotros
CORS(app)

@app.route('/')
def hello():
    return jsonify({
        "message": "¡Hola desde el Backend (Lab A)!",
        "status": "Online",
        "infra": "AWS ASG Monorepo"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)