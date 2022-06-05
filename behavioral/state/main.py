from player import Player
from state import ReadyState

if __name__ == "__main__":
    player = Player(ReadyState(None))
    player.click_next()
    player.click_previous()
    player.click_lock()
    player.click_play()
    player.click_lock()
    player.click_play()
    player.click_next()
    player.click_previous()
