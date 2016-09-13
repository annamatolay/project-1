class Thing:
    def __init__(self, **kwargs):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        for key, value in kwargs.items():
            setattr(self, key, value)


class Gate(Thing):
    @staticmethod
    def render():
        pass


class Portal(Thing):
    @staticmethod
    def render():
        pass


class Button(Thing):
    @staticmethod
    def render():
        pass


class Turner(Thing):
    @staticmethod
    def render():
        pass
