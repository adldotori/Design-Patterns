from button import Button


class Dialog(object):
    def __init__(self, os: str):
        self.button = Button.of(os)

    def render(self):
        self.button.onClick()
