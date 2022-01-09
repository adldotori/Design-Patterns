from dialog import Dialog


class Application(object):
    def __init__(self, os: str):
        self.dialog = Dialog.of(os=os)

    def run(self):
        self.dialog.render()


if __name__ == "__main__":
    app = Application(os="web")
    app.run()
