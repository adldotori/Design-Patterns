from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def onClick(self):
        raise NotImplementedError()


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


class Test(object):
    def test_windows(self):
        app = Application("windows")
        app.run()

    def test_html(self):
        app = Application("html")
        app.run()


if __name__ == "__main__":
    app = Application(os="html")
    app.run()
