import pygame

class Snake:
    def __init__(self, initial_body, direction):
        self.body = initial_body
        self.direction = direction

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, direction):
        self.direction = direction

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
            pygame.draw.rect(screen, (255, 255, 255), (segment[0]*10, segment[1]*10, 10, 10))
