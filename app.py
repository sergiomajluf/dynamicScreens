
from flask import Flask, render_template, request, jsonify
import requests
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

UNSPLASH_ACCESS_KEY = os.environ.get('aJBwHF-KwjHdwVbFZvFfswxEieGVJ6rT9pQlggAcGISg8U')

current_step = 1
step_content = {
    1: "Comencemos: Inicio de la Experiencia",
    2: "Paso 2: Progreso!",
    3: "Paso 3: Casi llegamos",
    4: "Paso 4: Etapa final",
    "default": "Paso desconocido"
}


def get_random_image_url():
    if not UNSPLASH_ACCESS_KEY:
        return 'https://images.unsplash.com/gifs/fail/fail-18.gif'
    
    headers = {'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'}
    response = requests.get('https://api.unsplash.com/photos/random?orientation=landscape', headers=headers)
    if response.status_code == 200:
        return response.json()['urls']['regular']
    else:
        return 'https://images.unsplash.com/gifs/fail/fail-18.gif'

@app.route('/')
def index():
    image_url = get_random_image_url()
    content = step_content[current_step]
    return render_template('index.html', step=current_step, content=content, image_url=image_url)

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/control_update')
def control_update():
    global current_step
    new_step = request.args.get('step', type=int)
    if new_step and 1 <= new_step <= 4:
        current_step = new_step
        content = step_content[current_step]
    else:
        content = step_content["default"]
    new_image_url = get_random_image_url()
    socketio.emit('update', {'step': current_step, 'content': content, 'image_url': new_image_url})
    return jsonify(success=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)