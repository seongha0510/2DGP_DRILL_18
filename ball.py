from pico2d import*
import random

class Ball:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class RandomBall:
    def __init__(self):
        self.x = random.randint(300,500)
        self.y = random.randint(600, 600)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class Ball:
    def __init__(self):
        self.x = random.randint(600, 800)
        self.y = random.randint(1200,1600)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)