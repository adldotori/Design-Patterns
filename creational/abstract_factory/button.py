from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def on_click(self):
        raise NotImplementedError()


class WindowsButton(Button):
    def __init__(self):
        pass

    def on_click(self):
        print("windows clicked")


class MacButton(Button):
    def __init__(self):
        pass

    def on_click(self):
        print("mac clicked")
