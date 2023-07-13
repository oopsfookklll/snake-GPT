import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, screen_size, snake, food):
        self.screen_size = screen_size
        self.snake = snake
        self.food = food
        self.score = 0
        self.game_over = False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_s:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_a:
                    self.snake.change_direction('left')
                elif event.key == pygame.K_d:
                    self.snake.change_direction('right')

    def update(self):
        if self.snake.move() == 'game_over':
            self.game_over = True
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            self.score += 1

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.snake.draw(screen)
        self.food.draw(screen)
        pygame.display.flip()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        clock = pygame.time.Clock()

        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw(screen)
            clock.tick(10)

        pygame.quit()
