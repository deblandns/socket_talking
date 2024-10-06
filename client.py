import socketio

sio = socketio.Client()


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
    sio.connect('http://localhost:5050')
    while True:
        msg = input("Enter message: ")
        sio.send(msg)


if __name__ == '__main__':
    main()
