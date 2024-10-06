import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('Connected to server')


@sio.event
async def disconnect():
    print('Disconnected from server')


@sio.event
async def message(data):
    print('Received message: ' + data)


def main():
    sio.connect('http://localhost:5000')
    while True:
        msg = input("Enter message: ")
        sio.send(msg)


if __name__ == '__main__':
    main()
