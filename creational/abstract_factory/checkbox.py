from abc import ABC, abstractmethod


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        raise NotImplementedError()


class WindowsCheckbox(Checkbox):
    def check(self):
        print("windows checked")


class MacCheckbox(Checkbox):
    def check(self):
        print("mac checked")
