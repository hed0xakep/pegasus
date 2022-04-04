class ConnectionError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        self.message = None

    def __str__(self):
        if self.message:
            return f'Connection failed, {self.message}'
        return 'Connection failed'
