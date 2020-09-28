class Die:
    import random

    def __init__(self, side):
        self.side = side
        self.die1 = None
        self.die2 = None

    def play(self, random=random):
        for i in range(10):
            self.die1 = random.randint(1, self.side)
            self.die2 = random.randint(1, self.side)
            print(self.die1, end=' ')
            print(self.die2)
            print()


new_game = Die(6)
new_game.play()

new_game = Die(10)
new_game.play()

new_game = Die(20)
new_game.play()
