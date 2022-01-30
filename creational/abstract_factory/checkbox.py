from abc import ABC, abstractmethod


class Checkbox(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def check(self):
        raise NotImplementedError()


class WindowsCheckbox(Checkbox):
    def __init__(self):
        pass

    def check(self):
        print("windows checked")


class MacCheckbox(Checkbox):
    def __init__(self):
        pass

    def check(self):
        print("mac checked")
