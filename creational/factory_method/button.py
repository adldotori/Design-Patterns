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

    def delete(self):
        print("delete button")


class HTMLButton(Button):
    def __init__(self):
        pass

    def on_click(self):
        self._hover()
        print("html clicked")

    def _hover(self):
        print("hover")
