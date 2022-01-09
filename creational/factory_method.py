from abc import ABC


class Button(ABC):
    def __init__(self):
        pass

    def onClick(self):
        print("clicked")


class WindowsButton(Button):
    def __init__(self):
        pass

    def onClick(self):
        print("windows clicked")


class HTMLButton(Button):
    def __init__(self):
        pass

    def onClick(self):
        print("html clicked")


class Application(object):
    def __init__(self, os: str):
        if os == "windows":
            self.button: Button = WindowsButton()
        elif os == "html":
            self.button: Button = HTMLButton()
        else:
            raise Exception("unknown os")

    def run(self):
        self.button.onClick()


if __name__ == "__main__":
    app = Application(os="html")
    app.run()
