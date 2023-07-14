import pygame
from snake import Snake
from food import Food
from ai_snake import AISnake
import random

class Game:
    def __init__(self, screen_size, snake, food):
        self.screen_size = screen_size
        self.snake = snake
        self.food = food
        self.score = 0
        self.game_over = False
        self.ai_snakes = []
        for  i in range(5):
            ai_snake = AISnake()
            self.ai_snakes.append(ai_snake)
        pygame.font.init() 
        self.font = pygame.font.Font(None, 32)

    def render_score(self, screen):
        score_text = f"Score: {self.score}"  
        score_image = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(score_image, (10, 10))

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
        for ai_snake in self.ai_snakes:
            ai_snake.update(self.food) # pass food for targeting
        if self.snake.move() == 'game_over':
            self.game_over = True
        if self.snake.eat(self.food):
            r = random.randint(0, 255)
            g = random.randint(0, 255) 
            b = random.randint(0, 255)
            self.snake.color = (r, g, b)
            self.score += 1
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            self.score += 1

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for ai_snake in self.ai_snakes:
            ai_snake.draw(screen)
        self.render_score(screen)
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
