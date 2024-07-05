class Events:

    def __init__(self):

        self.windows = None
        self.window = None

    def events(self, event, modules):

        if self.windows.uniqid is None:
            self.windows.uniqid = None

        if event == "button_1":
            self.window.update([{
                "key": "in_line_2",
                "mode": "replace",
                "value": self.window.get_item("in_line_1")
            }])

