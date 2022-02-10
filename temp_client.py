import json
import sys

import socketio

if len(sys.argv) != 2:
    print("Usage: python3 temp_client.py <player_id>")
    exit(1)

sio = socketio.Client()

if sys.argv[1] == "1":
    PLAYER_ID = 'player1'
    PLAYER_PASSWORD = 'player1'
else:
    PLAYER_ID = 'player2'
    PLAYER_PASSWORD = 'player2'
PLAYER_ROOM = 'room1'


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def action(state):
    print('State: ', state)
    print(type(state))
    target = (0, 1) if PLAYER_ID == 'player1' else (1, 0)
    action = {
        "action_type": 'MOVE',
        "troop": "Gamora",
        'target': target,
        'player_id': PLAYER_ID,
        'player_password': PLAYER_PASSWORD,
        'round_no': state['round_no']

    }

    sio.emit('action', action)


@sio.event
def my_response(data):
    print("Response:", data)


sio.connect('http://127.0.0.1:8000',
            {"auth": json.dumps({'player_id': PLAYER_ID, 'password': PLAYER_PASSWORD, 'room': PLAYER_ROOM})})