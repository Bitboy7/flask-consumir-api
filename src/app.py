from flask import Flask, render_template, request
import requests

# Crear instancia del objeto WSGI (Web Server Gateway Interface)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # Renderizar plantilla HTML para mostrar el formulario

@app.route('/submit', methods=['POST'])
def submit():
    data = {
    'IdDoctor': int(request.form['id']),
    'Nombre': request.form['nombre'],
    'Especialidad': request.form['especialidad'],
    'HospitalId': int(request.form['hospital_id'])
}
    
    response = requests.post("https://meditrack-production.up.railway.app/doctores/create/", json=data)
    if response.status_code == 200:
        message = f"Se ha creado correctamente al doctor {response.json()}"
    else:
        message = f"Error en la petición HTTP: {response.text}"
        
    return render_template('list.html', message=message) # Mostrar mensaje o resultado

if __name__ == '__main__':
    app.run()