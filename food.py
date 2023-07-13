import pygame
import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 49), random.randint(0, 49))

    def randomize_position(self):
        self.position = (random.randint(0, 49), random.randint(0, 49))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0]*10, self.position[1]*10, 10, 10))
