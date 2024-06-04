from flask import Flask, render_template, request
from clases import Usuario
 
app = Flask(__name__)
 
# Ruta para el formulario de entrada de datos
@app.route('/')
def formulario():
    return render_template('formulario.html')
 
# Ruta para procesar los datos del formulario
@app.route('/registrar', methods=['POST'])
def calcular():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return render_template('resultado.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

