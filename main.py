from game import Game
from snake import Snake
from food import Food

def main():
    initial_position = [(25, 25)]
    initial_direction = 'up'
    snake = Snake(initial_position, initial_direction)
    food = Food()
    game = Game((500, 500), snake, food)
    game.run()

if __name__ == "__main__":
    main()
