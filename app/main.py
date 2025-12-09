from flask import Flask, jsonify

app = Flask(__name__)

# Ruta principal - nuestro "Hola Mundo"
@app.route('/')
def home():
    return jsonify({
        "mensaje": "¡Hola desde Flask!",
        "status": "success",
        "version": "1.0.0"
    })

# Ruta de salud - para checkear que todo funciona
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "code": 200
    })

# Ruta de API - ejemplo de endpoint más complejo
@app.route('/api/saludar/<nombre>')
def saludar(nombre):
    return jsonify({
        "mensaje": f"¡Hola, {nombre}! Bienvenido a CI/CD",
        "nombre": nombre
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)