from game import Game
from snake import Snake
from food import Food

def main():
    snake = Snake([(25, 25)], 'up')
    food = Food()
    game = Game((500, 500), snake, food)
    game.run()

if __name__ == "__main__":
    main()
