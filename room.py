import socket
from random import choice
from string import ascii_uppercase
import datetime
from exceptions import ConnectionError

class Room:

    def __init__(self, max_cons: int):
        self.token = ''.join(choice(ascii_uppercase) for i in range(6))
        self.connections = []
        self.MAX_CONNECTIONS = max_cons

    def send_msg(self, msg: str, user=None):
        if user:
            msg_time = datetime.datetime.now()
            msg = f'{msg_time.hour}:{msg_time.minute} | {user}: {msg}'
        for user in self.connections:
            user.send(msg.encode())

    def connect(self, user, token):
        if token != self.token:
            raise ConnectionError(f'invalid access token: {token}')
        if len(self.connections) >= self.MAX_CONNECTIONS:
            raise ConnectionError(f'the room is full, max connetions - {self.MAX_CONNECTIONS}')
        if not user in self.connections:
            self.connections.append(user)
            send_msg(f"-------> {user} connected to the server")
