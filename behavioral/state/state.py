from abc import ABC, abstractmethod
from player import Player


class State(ABC):
    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def click_lock(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self):
        pass

    @abstractmethod
    def click_previous(self):
        pass


class ReadyState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.change_state(PlayingState(self.player))

    def click_next(self):
        print("Move on to the next song")

    def click_previous(self):
        print("Move on to the previous song")


class PlayingState(State):
    def click_lock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self):
        self.player.change_state(ReadyState(self.player))

    def click_next(self):
        print("Play the next song")

    def click_previous(self):
        print("Play the previous song")


class LockedState(State):
    def click_lock(self):
        self.player.change_state(ReadyState(self.player))

    def click_play(self):
        pass

    def click_next(self):
        pass

    def click_previous(self):
        pass
