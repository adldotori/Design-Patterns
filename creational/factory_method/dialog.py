from abc import ABC, abstractmethod

from button import WindowsButton, HTMLButton


class Dialog(ABC):
    @classmethod
    def of(cls, os: str):
        if os == "windows":
            return WindowsDialog()
        elif os == "web":
            return WebDialog()
        else:
            raise KeyError("unknown os")

    @abstractmethod
    def render(self):
        raise NotImplementedError()


class WindowsDialog(object):
    def __init__(self):
        self.button = WindowsButton()

    def render(self):
        print("turn on windows")
        self.button.on_click()
        self.button.delete()


class WebDialog(object):
    def __init__(self):
        self.button = HTMLButton()

    def render(self):
        print("turn on web")
        self.button.on_click()
