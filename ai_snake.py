# ai_snake.py

import random
from snake import Snake
MAX_WIDTH = 500 
MAX_HEIGHT = 500

class AISnake(Snake):

    def __init__(self):
        initial_body = [(10,10)]
        direction = 'up'
        super().__init__(initial_body, direction)
        self.direction = random.choice(['up','down','left','right'])

    def update(self, food):
        next_pos = self.head 
        if self.direction == 'up':
            next_pos = (next_pos[0], next_pos[1] - 1)
        elif self.direction == 'down':
            next_pos = (next_pos[0], next_pos[1] + 1)
        elif self.direction == 'left':
            next_pos = (next_pos[0] - 1, next_pos[1])
        elif self.direction == 'right':  
            next_pos = (next_pos[0] + 1, next_pos[1])

        # Check for collisions
        if next_pos in self.body or next_pos[0] < 0 or next_pos[0] >= MAX_WIDTH or next_pos[1] < 0 or next_pos[1] >= MAX_HEIGHT:
            self.direction = random.choice(['up','down','left','right'])
        else:
            self.body.insert(0, next_pos)
            self.body.pop()

        # Occasionally change directions randomly
        if random.random() < 0.1:
            self.direction = random.choice(['up','down','left','right'])