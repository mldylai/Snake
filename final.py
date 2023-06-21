import pygame
from pygame.locals import *
import time
import random
import unittest

"""
1. Download pygame 
To install pygame, navigate to your terminal/command prompt
For Windows, type in:
py -m pip install -U pygame
For Mac, type in:
python3 -m pip install -U pygame

2. Unzip your zip file into a folder in your computer. Make sure there are five files:
test.py
final.py
three images within “image assets”

3. Start running the program by navigating to the file that contains this code (final.py)
For example, the file is in Documents. Go to the terminal and type in "cd Documents" then “cd final_project” then "python3 final.py". 
Then, you are good to start playing the game! The snake will start running automatically

"""



DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500

class Apple: 
    def __init__(self):
        self.image = pygame.image.load("image assets/apple.png").convert_alpha()
        self.x = 150
        self.y = 150

    def add_new_apple(self):
        """this function takes no input and return a list containing a random x coordinate 
        and a random y coordinate"""

        self.x = random.randrange(0, 500, 25)
        self.y = random.randrange(0, 500, 25)
        return [self.x, self.y]


class Score:
    def __init__(self):
        self.score = 0

    def display_score(self, score, font_size):
        """function takes in the score value, the font size
        and return the render of the graphic of the score that contains the color and the font size"""

        font = pygame.font.Font('freesansbold.ttf', font_size)
        score_render = font.render('Score: ' + str(self.score), True, (255,255,255))
        return score_render


class Snake:
    def __init__(self, head_image, body_image):
        self.body_image = body_image
        self.head_image = head_image
        self.x = 250
        self.y = 250
        self.body = [[250,225], [250,200], [250, 175]]
        self.direction = 'down'

    def move(self):
        '''Takes no input and changes self.body according to the current value of self.direction.
        This function is called when we want the snake to move and the snake has not hit an apple. '''

        if self.direction == 'up':
            #self.body.insert(0, [self.x, self.y])
            self.move_when_collide()
            self.body.pop(-1)
        elif self.direction == 'down':
            self.move_when_collide()
            self.body.pop(-1)
        elif self.direction == 'left':
            self.move_when_collide()
            self.body.pop(-1)
        elif self.direction == 'right':
            self.move_when_collide()
            self.body.pop(-1)

    def move_when_collide(self):

        '''Takes no input and changes self.body according to the current value of self.direction.
        This function is called when we want the snake to move and the snake hits an apple. 
        Basically the snake's length is increased by one 25x25 block.'''

        if self.direction == 'up':
            self.body.insert(0, [self.x, self.y])
            self.move_up()
        elif self.direction == 'down':
            self.body.insert(0, [self.x, self.y])
            self.move_down()
        elif self.direction == 'left':
            self.body.insert(0, [self.x, self.y])
            self.move_left()
        elif self.direction == 'right':
            self.body.insert(0, [self.x, self.y])
            self.move_right()

    def is_hit_boundary(self):
        """this function takes in no input and returns True if the Snake goes outside the boundary 
        of the board"""

        if (self.x >= 500 and self.direction == 'right' or self.x < 0 and self.direction == 'left') or\
             (self.y >= 500 and self.direction == 'down' or self.y < 0 and self.direction == 'up'):
            return True
        else:
            return False

    def eat_apple(self, x, y):
        """the function takes in an x value and a y value and return True if the x and y value are
        both equal to the self.x and self.y respectively. Returns False otherwise. This function is used to 
        test if the Snake's head collides with an apple"""

        if x == self.x and y == self.y:
            return True
        else: 
            return False

    def is_empty(self, x, y):
        """takes in an x value and a y value. Returns False if the x,y coordinate pair is found in the 
        self.body list or if self.x equals the x value and self.y equals the y value. This function is
        used to check if the x, y coordinate inputted has been occupied by the Snake head or body. If not,
        it's considered an empty position, which is eligible for an Apple to be added"""


        # compare with body
        for i in range(len(self.body)):
            if [x,y] in self.body[i]:
                return False
                
        # compare with head
        if self.x == x and self.y == y:
            return False
        else:
            return True

    def is_hit_body(self):
        '''takes in no input and returns True when the snake collides with itself, 
        meaning that the x and y position of the head repeats in the self.body. Else, return False'''

        if [self.x, self.y] in self.body:
            return True


#these four functions move up the snake's head by changing self.direction and modifying its xy coordinates

    def move_up(self):
        
        self.direction = 'up'
        self.y = self.y - 25

    def move_down(self):
        
        self.direction = 'down'
        self.y = self.y + 25

    def move_left(self):
        
        self.direction = 'left'
        self.x = self.x - 25

    def move_right(self):
        
        self.direction = 'right'
        self.x = self.x + 25


def main():
    pygame.init()

    #set up a clock
    clock = pygame.time.Clock()

    #set up the board, fill the board with color black
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 32)

    gameDisplay.fill((000, 000, 000))

    #create snake, apple, score object
    snake = Snake(pygame.image.load("image assets/snake_head.png").convert_alpha(), pygame.image.load("image assets/snake_body.jpg").convert_alpha()) 
    apple = Apple()
    score = Score()

    #rescale the snake and the apple visualization
    width = 25 
    snake.head_image = pygame.transform.scale(snake.head_image, (width, width))   
    snake.body_image = pygame.transform.scale(snake.body_image, (width, width))  
    apple.image = pygame.transform.scale(apple.image, (width, width))

    while True:

        for event in pygame.event.get():
            # Quits the game if the pygame window is ever closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                elif event.key == pygame.K_UP:
                    if snake.direction != 'down':
                        snake.direction = 'up'
                    

                elif event.key == pygame.K_DOWN:
                    if snake.direction != 'up':
                        snake.direction = 'down'


                elif event.key == pygame.K_RIGHT:
                    if snake.direction != 'left':
                        snake.direction = 'right'


                elif event.key == pygame.K_LEFT:
                    if snake.direction != 'right':
                        snake.direction = 'left'


        if snake.is_hit_boundary() == True or snake.is_hit_body() == True:
            break

        if snake.eat_apple(apple.x, apple.y) == True:
            snake.move_when_collide()
            new_coordinate = apple.add_new_apple()
            score.score += 1
            while snake.is_empty(new_coordinate[0], new_coordinate[1]) == False:
                new_coordinate =  apple.add_new_apple()
            apple.x = new_coordinate[0]
            apple.y = new_coordinate[1]
        else:
            snake.move()

        
        gameDisplay.fill((000, 000, 000))
        gameDisplay.blit(snake.head_image, (snake.x, snake.y))
        gameDisplay.blit(apple.image, (apple.x, apple.y))
        for i in range(len(snake.body)):
            gameDisplay.blit(snake.body_image, (snake.body[i][0], snake.body[i][1]))
        gameDisplay.blit(score.display_score(score.score, 16), (1,1))

        pygame.display.update()
        time.sleep(0.25)


if  __name__ == "__main__":
    main()
