class Button(object):
    def __init__(self):
        pass

    def onClick(self):
        print("clicked")


class Application(object):
    def __init__(self, button: Button):
        self.button = button

    def run(self):
        self.button.onClick()


if __name__ == "__main__":
    button = Button()
    app = Application(button)
    app.run()
