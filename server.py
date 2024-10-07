from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_socketio import SocketIO, send
from flashtext import KeywordProcessor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['JWT_SECRET_KEY'] = 'Jwt_secret!'
socketio = SocketIO(app)
jwt = JWTManager(app)

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('!', '')
keyword_processor.add_keyword('@', '')
keyword_processor.add_keyword('#', '')
keyword_processor.add_keyword('/', '')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Validate username and password (this is just an example)
    if username == 'user' and password == 'pass':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@socketio.on('message')
@jwt_required()
def handle_message(msg):
    sanitized_msg = keyword_processor.replace_keywords(msg)
    print('Message: ' + sanitized_msg)
    send(sanitized_msg, broadcast=True)


if __name__ == '__main__':
    print("server is running ..")
    socketio.run(app, host='0.0.0.0', port=7062)