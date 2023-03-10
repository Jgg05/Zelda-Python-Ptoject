import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		pygame.display.set_caption ('Zelda')
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
<<<<<<< HEAD
<<<<<<< HEAD
	game.run()	
	#test 2
	#Test 3
=======
	game.run()	
>>>>>>> Test
=======
	game.run()	
	#test 2
	#Test 3
>>>>>>> 8d45cc2218de550939d94ebd8855605695d43bfc
