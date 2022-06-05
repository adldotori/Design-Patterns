from player import Player
from state import ReadyState, PlayingState, LockedState


def test():
    player = Player(ReadyState(None))
    assert player.state.__class__.__name__ == "ReadyState"

    player.click_next()
    player.click_previous()
    player.click_lock()
    assert player.state.__class__.__name__ == "LockedState"

    player.click_play()
    player.click_lock()
    player.click_play()
    assert player.state.__class__.__name__ == "PlayingState"

    player.click_next()
    player.click_previous()
