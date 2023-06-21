import unittest
from final import *

class Test(unittest.TestCase):

	def test_is_empty(self):

		test_snake = Snake("image_head","image_body")

		self.assertEqual(test_snake.is_empty(250,250), False)
		self.assertEqual(test_snake.is_empty(100,100), True)
		

	def test_eat_apple(self):

		test_snake = Snake("image_head","image_body")

		self.assertEqual(test_snake.eat_apple(250,250), True)
		self.assertEqual(test_snake.eat_apple(100,100), False)


if  __name__ == "__main__":
    unittest.main()

