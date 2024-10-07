import socketio
import requests

sio = socketio.Client()

def get_jwt_token():
    response = requests.post('http://localhost:7062/login', json={'username': 'user', 'password': 'pass'})
    return response.json().get('access_token')

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def message(data):
    print('Received message: ' + data)

def main():
    token = get_jwt_token()
    sio.connect('http://localhost:7062', headers={'Authorization': f'Bearer {token}'})
    while True:
        msg = input("Enter message: ")
        sio.send(msg)

if __name__ == '__main__':
    main()
