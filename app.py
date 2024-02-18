from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    socketio.send(message)  # Envia a mensagem para todos os clientes conectados

if __name__ == '__main__':
    # Modifique a linha abaixo para usar o novo endereço fornecido pelo ngrok e a porta do localhost
    socketio.run(app, host='localhost', port=5000)



