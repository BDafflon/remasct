import copy
import json

import eventlet
import socketio
import threading
import time

from sma.environment.environment import Environment

simulation = Environment()
control = {"speed":1,"play":True}

def thread_function(name):
    print("start sim")
    i=0
    while True:
        time.sleep(0.1)
        if control["play"]:
            simulation.run(control["speed"])
 


sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    

    

@sio.event
def my_message(sid, data):
    print('message ', data)
    sio.emit('my_message', "hello from server")   


@sio.on('update-speed')
def update_speed(sid,d):
    global control
    control["speed"]=max(0.1,control["speed"]+d)
    print(control)

@sio.on('update-stop')
def update_stop(sid):
    global control, simulation
    simulation = Environment()
    control = {"speed":1,"play":True}

@sio.on('update-play-pause')
def update_play_pause(sid, data):
    global control
    control["play"]=data
    

@sio.on('create-something')
def another_event(sid, data):
    agentList = simulation.agents.copy()
    itemList = simulation.items.copy()
    serializedAgents=[]
   
    for a in agentList:
        serializedAgent={"uuid":a.uuid,"type":a.type,"body":{"pos":a.body.pos,"visible":a.body.visible}}
        serializedAgents.append(serializedAgent)


     
    sio.emit('update', json.dumps({"agents":serializedAgents,"items":[],"control":control}))

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__': 
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5050)), app)
    