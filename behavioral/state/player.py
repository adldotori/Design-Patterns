class Player(object):
    def __init__(self, state):
        self.state = state
        self.state.player = self

    def change_state(self, state):
        print(
            f"Change state: {self.state.__class__.__name__} -> {state.__class__.__name__}"
        )
        self.state = state

    def click_lock(self):
        print("Click the lock button")
        self.state.click_lock()

    def click_play(self):
        print("Click the play button")
        self.state.click_play()

    def click_next(self):
        print("Click the next button")
        self.state.click_next()

    def click_previous(self):
        print("Click the previous button")
        self.state.click_previous()
