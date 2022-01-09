from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self):
        pass

    @classmethod
    def of(cls, os: str):
        if os == "windows":
            return WindowsButton()
        elif os == "html":
            return HTMLButton()
        else:
            raise KeyError("unknown os")

    @abstractmethod
    def on_click(self):
        raise NotImplementedError()


class WindowsButton(Button):
    def __init__(self):
        pass

    def on_click(self):
        print("windows clicked")


class HTMLButton(Button):
    def __init__(self):
        pass

    def on_click(self):
        print("html clicked")
