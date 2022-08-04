import websocket, json

class WebsocketHelper:
    def __init__(self, url: str) -> None:
        self.gatewayURL = url
        self.wss = websocket.WebSocket()

    def connectToSocket(self):
        try:
            self.socket = self.wss.connect(self.gatewayURL)
            print('Connected to socket')
        except Exception as e:
            print(e)
            return False

    def receivePayload(self):
        for m in self.wss:
            payload = json.loads(str(m))
            return payload