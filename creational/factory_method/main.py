from button import Button


class Application(object):
    def __init__(self, os: str):
        self.button = Button.of(os)

    def run(self):
        self.button.onClick()


if __name__ == "__main__":
    app = Application(os="html")
    app.run()
