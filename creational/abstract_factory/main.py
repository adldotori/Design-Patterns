from factory import GUIFactory


class Application(object):
    def __init__(self, os: str):
        self.factory = GUIFactory.of(os=os)

    def run(self):
        button = self.factory.createButton()
        checkbox = self.factory.createCheckbox()

        button.on_click()
        checkbox.check()


if __name__ == "__main__":
    app = Application(os="windows")
    app.run()
