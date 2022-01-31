from abc import ABC, abstractmethod

from button import Button, WindowsButton, MacButton
from checkbox import Checkbox, WindowsCheckbox, MacCheckbox


class GUIFactory(ABC):
    @classmethod
    def of(cls, os: str):
        if os == "windows":
            return WindowsFactory()
        elif os == "mac":
            return MacFactory()
        else:
            raise KeyError("unknown os")

    @abstractmethod
    def createButton(self) -> Button:
        raise NotImplementedError()

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        raise NotImplementedError()


class WindowsFactory(GUIFactory):
    def createButton(self) -> Button:
        return WindowsButton()

    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()
