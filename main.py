import json
import threading
import time
from datetime import datetime

import eventlet
import socketio

from Action import Action

eventlet.monkey_patch()

from Environment import Environment
from Player import Player

rooms = {
    'room1': {
        'id': 'room1',
        'start_time': "Feb 10 2022  7:48PM +0530",
        'player1': {
            'player_id': 'player1',
            "password": "player1",
        },
        'player2': {
            'player_id': 'player2',
            "password": "player2",
        }
    },
}


def run(sio, room_id):
    """
    Main function
    """

    if room_id not in rooms.keys():
        return False

    # convert time string to timestamp
    start_time = datetime.strptime(rooms[room_id]['start_time'], '%b %d %Y %I:%M%p %z')
    print(start_time)
    start_time = start_time.timestamp()
    print(start_time)
    print(time.time())
    print(start_time - time.time())
    start_time = time.time() + 10
    env = Environment(room_id, start_time, 20, 20, 30, 1, 1, )
    env.create_graph()

    env.print_graph()
    print(env.is_graph_connected())

    # env.place_special_cells(3, 2, 2, 2)

    print(env.get_graph()[0][0].get_cell_type())

    update_rounds = threading.Thread(target=env.update_rounds, args=(sio,))
    update_rounds.start()

    # sio.start_background_task(env.update_rounds, sio)

    # print(env.get_player1().get_guardians())


def create_socket():
    # create a Socket.IO server
    sio = socketio.Server(async_mode='eventlet')
    # wrap with a WSGI application
    app = socketio.WSGIApp(sio)

    return sio, app


# Press the green button in the gutter to run the script.
def main():
    sio, app = create_socket()

    ROOM_ID = 'room1'

    if ROOM_ID not in rooms.keys():
        return False

        # convert time string to timestamp
    start_time = datetime.strptime(rooms[ROOM_ID]['start_time'], '%b %d %Y %I:%M%p %z')
    print(start_time)
    start_time = start_time.timestamp()
    print(start_time)
    print(time.time())
    print(start_time - time.time())
    start_time = time.time() + 10
    env = Environment(ROOM_ID, start_time, 20, 20, 30, 1, 0, )
    env.create_graph()

    env.print_graph()
    print(env.is_graph_connected())

    # env.place_special_cells(3, 2, 2, 2)

    print(env.get_graph()[0][0].get_cell_type())

    update_rounds = threading.Thread(target=env.update_rounds, args=(sio,))
    update_rounds.start()

    @sio.event
    def action(sid, data):
        if sid == env.get_player1().get_socket_id():
            print("player1 action")
            env.add_action_to_player1(Action.get_obj_from_json(data))
        elif sid == env.get_player2().get_socket_id():
            print('Player 2 action')
            env.add_action_to_player2(Action.get_obj_from_json(data))
        else:
            print('invalid user')

        print(sid, data, type(data))

    @sio.on('connect')
    def connect(sid, environ):
        global rooms
        print("connect ", sid)
        # print(environ['HTTP_AUTH'], type(environ['HTTP_AUTH']))

        if 'HTTP_AUTH' in environ:
            auth_details = json.loads(environ['HTTP_AUTH'])
        else:
            auth_details = None
            print("no auth details")
            sio.disconnect(sid)
            return False

        print(auth_details)
        if auth_details['room'] in rooms.keys():
            if auth_details['player_id'] == rooms[auth_details['room']]['player1']['player_id']:
                if auth_details['password'] == rooms[auth_details['room']]['player1']['password']:
                    if env.get_player1() is None:
                        env.set_player1(Player(auth_details['player_id'], sid, env.get_graph()[0][0]))
                        print("player1 connected")
                    else:
                        if not env.get_player1().is_connected():
                            env.get_player1().set_player_id(sid)
                            env.get_player1().set_connected(True)
                            print("player1 reconnected")
                        else:
                            print("player1 already connected")
                else:
                    print("wrong password for player1")
                    sio.disconnect(sid)
                    return False
            elif auth_details['player_id'] == rooms[auth_details['room']]['player2']['player_id']:
                if auth_details['password'] == rooms[auth_details['room']]['player2']['password']:
                    if env.get_player2() is None:
                        env.set_player2(Player(auth_details['player_id'], sid, env.get_graph()[0][0]))
                        print("player2 connected")
                    elif not env.get_player2().is_connected():
                        env.get_player2().set_player_id(sid)
                        env.get_player2().set_connected(True)
                        print("player2 reconnected")
                    else:
                        print("player2 already connected")
                else:
                    print("wrong password for player2")
                    sio.disconnect(sid)
                    return False
            else:
                print("wrong username")
                sio.disconnect(sid)
                return False
        else:
            print("wrong room")
            sio.disconnect(sid)
            # print all connected users to the socket

            return False

        sio.emit('my_response', {'data': 'Connected'})

    @sio.on('disconnect')
    def disconnect(sid):
        print('disconnect ', sid)
        if env.get_player1().get_socket_id() == sid:
            env.get_player1().set_connected(False)
            env.get_player1().set_socket_id(None)
            print("player1 disconnected")
        elif env.get_player2().get_socket_id() == sid:
            env.get_player2().set_connected(False)
            env.get_player2().set_socket_id(None)
            print("player2 disconnected")
        else:
            print("disconnecting unknown player")

    # start the server

    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)


if __name__ == '__main__':
    main()
