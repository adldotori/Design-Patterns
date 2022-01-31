from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def on_click(self):
        raise NotImplementedError()


class WindowsButton(Button):
    def on_click(self):
        print("windows clicked")


class MacButton(Button):
    def on_click(self):
        print("mac clicked")
