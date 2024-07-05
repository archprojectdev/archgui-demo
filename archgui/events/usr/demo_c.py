class Events:

    def __init__(self):

        self.windows = None
        self.window = None

    def events(self, event, modules):

        if self.windows.uniqid is None:
            self.windows.uniqid = None

