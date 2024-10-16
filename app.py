
from flask import Flask, render_template, request, jsonify
import requests
from flask_socketio import SocketIO, emit
import os

# Cargar variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Configura tu clave de API de Unsplash (para las imágenes de fond
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

# Crea un dicionario de respuestas para enviar al cliente html
current_step = 1
step_content = {
    1: "Comencemos: Inicio de la Experiencia",
    2: "Paso 2: Progreso!",
    3: "Paso 3: Casi llegamos",
    4: "Paso 4: Etapa final",
    "default": "Paso desconocido"
}

# Llama a Unspash para obtener una imagen random cada vez que sea necesario
def get_random_image_url():
    if not UNSPLASH_ACCESS_KEY:
        return 'https://images.unsplash.com/gifs/fail/fail-18.gif'
    
    headers = {'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'}
    response = requests.get('https://api.unsplash.com/photos/random?orientation=landscape', headers=headers)
    if response.status_code == 200:
        return response.json()['urls']['regular']
    else:
        return 'https://images.unsplash.com/gifs/fail/fail-18.gif'

# La ruta principal, para mostrar el HTML que será controlado remotamente
@app.route('/')
def index():
    # obtiene la imagen desde la función aleatoria
    image_url = get_random_image_url()
    # obtiene el contenido desde el diccionario interno
    content = step_content[current_step]
    # envia la respuesta adjuntando datos que son usados en la plantilla html
    return render_template('index.html', step=current_step, content=content, image_url=image_url)

# Esta ruta solamente muestra el listado de links
@app.route('/control')
def control():
    return render_template('control.html')

# Esta es la ruta que recibe la instrucción externa. La procesa obteniendo desde la URL el parametro step
# Con ese parámetro, obtiene el contenido correcto del diccionario interio
# Finalmente usa socket io para enviar los datos hacia el cliente html.
# En el cliente (ver plantilla index.html), socket se encarga de la actualización a traves e la función socket.on('update', function(data)
@app.route('/control_update')
def control_update():
    global current_step
    new_step = request.args.get('step', type=int)
    if new_step and 1 <= new_step <= 4:
        current_step = new_step
        content = step_content[current_step]
    else:
        content = step_content["default"]
        current_step = "error"
    new_image_url = get_random_image_url()
    socketio.emit('update', {'step': current_step, 'content': content, 'image_url': new_image_url})
    return jsonify(success=True)

# Esta linea inica el servidor, define la IP y el puerto
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)