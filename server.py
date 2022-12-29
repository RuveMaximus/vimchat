from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def send_message(sid, message):
    await sio.emit('receive_message', {'message': message, 'from': sid}, room=message.get('chat'))

@sio.event 
async def connect_to_chat(sid, data):
    sio.enter_room(sid, data)
    await sio.emit('connected_to_chat', f"new in chat: {sid}", room=data)
    return 'connected to %s' % [data]

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)