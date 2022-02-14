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
PLAYER_ROOM = 'room12'


@sio.event
def connect():
    print("I'm connected!")

counter = 1

@sio.event
def action(state):
    global counter
    print('State: ', state)
    print(type(state))

    # save feedback files
    fi = open('feedback.json', 'a')
    fi.write(json.dumps(state['feedback']) + '\n')
    fi.close()

    if PLAYER_ID == 'player1':
        target = (0, counter)
        action = {
            "action_type": 'SPECIAL',
            "troop": "Drax",
            'target': '(3, 5)',
            'player_id': PLAYER_ID,
            'round_no': state['round_no']
        }
        counter += 1
    else:
        action = {
            "action_type": 'MOVE',
            "troop": "Gamora",
            'target': '(0, 1)',
            'player_id': PLAYER_ID,
            'round_no': state['round_no']

        }

    # save action to file
    fi = open('action.json', 'w')
    json.dump(action, fi)

    fi.close()

    sio.emit('action', action)


@sio.event
def connected(data):
    print("Response:", data)


sio.connect('http://127.0.0.1:5000',
            {"auth": json.dumps({'player_id': PLAYER_ID, 'password': PLAYER_PASSWORD, 'room': PLAYER_ROOM})})
