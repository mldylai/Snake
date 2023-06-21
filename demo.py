import pygame
import random
import time

#pygame.init()
#clock = pygame.time.Clock()
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)
w = 500
h = 500
size_square = 25
board_size = [w, h]
#board = pygame.display.set_mode(board_size)

class createSquare:
	def __init__(self, width, color):
		self.w = width
		self.color = color

	def get_square(self):
		return [self.w]

class Snake
	def __init__(self,board):
		self.x = x
		self.y = y 
		self.square_object= createSquare(25, GREEN)
		self.head = self.square_object.get_square()
		self.head.append(self.x)
		self.head.append(self.y)
		self.tail = self.square_object.get_square()
		self.tail.append(self.x)
		self.tail.append(self.y-25)
		self.body = [self.head, self.tail]
		#pygame.draw.rect(board,GREEN,[snake1.x,snake1.y,25,25])
		#pygame.draw.rect(board,GREEN,[snake1.x,snake1.y-25,25,25])

	def move_up(self):
		for item in range(len(self.body)):
			square = self.body[item]
			square[2]= square[2] - size_square


		return self.body

	def move_down(self):
		for item in range(len(self.body)):
			square = self.body[item]
			square[2]= square[2] + size_square

		return self.body

	def move_right(self):
		for item in range(len(self.body)):
			square = self.body[item]
			square[1]= square[1] + size_square

		return self.body

	def move_left(self):
		for item in range(len(self.body)):
			square = self.body[item]
			square[1] = square[1] - size_square

		return self.body

	'''def eat_Apple(self):
		apple_position = Apple.get_position()
		if self.x == apple_position[0] and self.y == apple_position[1]:
			print('hello')'''


'''class Apple:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.square_object= createSquare(25, RED)
		self.square = self.square_object.get_square()
		self.square.append(self.x)
		self.square.append(self.y)

	def get_position(self):
		return [self.x, self.y]'''





	





	
