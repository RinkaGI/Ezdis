import websocket
from Ezdis.wss import WebsocketHelper

class Bot:
    def __init__(self) -> None:
        self.gatewayURL = 'wss://gateway.discord.gg/?v=9&encoding=json'
        self.socket = WebsocketHelper(self.gatewayURL)

        self.socket.connectToSocket()
        print(self.socket.receivePayload())