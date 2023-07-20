import pygame

class Snake:
    def __init__(self, initial_body=None, direction="up", color=(0, 0, 255)):
        if initial_body is None:
           initial_body = [(10,10)]
        self.body = initial_body
        self.direction = direction
        self.color = color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, direction):
        self.direction = direction

    def eat(self, food):
        if self.head == food.position:
            return True
        else:
            return False

    def move(self):
        if self.direction == 'up':
            new_head = (self.head[0], self.head[1] - 1)
        elif self.direction == 'down':
            new_head = (self.head[0], self.head[1] + 1)
        elif self.direction == 'left':
            new_head = (self.head[0] - 1, self.head[1])
        elif self.direction == 'right':
            new_head = (self.head[0] + 1, self.head[1])

        if new_head in self.body or new_head[0] < 0 or new_head[0] >= 50 or new_head[1] < 0 or new_head[1] >= 50:
            return 'game_over'

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0]*10, segment[1]*10, 10, 10))
