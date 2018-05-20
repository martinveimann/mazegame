#2 button flappyJoust

import pygame
import time

ekraan = pygame.display.set_mode((800, 600))


porand_pilt = pygame.image.load("sein.png")
player_pilt = pygame.image.load("uus_kast.png")
enemy_pilt = pygame.image.load("kuri_ring.png")
ekraan.blit(porand_pilt, (0, 200))
"""
#map layout
################



#####------#####



----########----


---##########---
"""
map = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10],
[39, 10], [38, 10], [37, 10], [36, 10], [35, 10], [34, 10], [33, 10], [32, 10], [31, 10], [30, 10]]



class player(pygame.sprite.Sprite):

	def __init__(self):
		
		self.xSpeed = 5
		self.ySpeed = 0
		self.direction = 1

		pygame.sprite.Sprite.__init__(self)
		self.image = player_pilt
		self.rect = self.image.get_rect()

		self.rect.x = 100
		self.rect.y = 100

	def jump(self):
		self.xSpeed += 0.08
		if self.ySpeed <= -2:
			self.ySpeed = -12
		else:
			self.ySpeed = -10

	def changeDirection(self):
		self.direction = self.direction * -1
		if self.xSpeed > 3:
			self.xSpeed = self.xSpeed * 0.9

	def nextFramePosition(self):
		if self.rect.x >= 780 and self.direction == 1:
			self.rect.x = 0

		elif self.rect.x <= 0 and self.direction == -1:
			self.rect.x = 780

		self.rect.x += self.xSpeed * self.direction
		if self.rect.y <= 20 and self.ySpeed < 0:
			self.ySpeed = self.ySpeed * -1

		self.rect.y += self.ySpeed
		self.ySpeed += 1

	#def collisionDetector():

		#todo collision detection and concequenses

class enemy(player):

	def __init__(self):
		player.__init__(self)
		self.rect.x = 720
		self.direction = -1
		self.jumpCD = 0 #jump cooldown for AI
		self.directionCD = 0 #direction change cooldown for AI
		self.image = enemy_pilt

	def AI(self, playerPosition):
		self.jumpCD -= 1
		self.directionCD -=1

		if self.jumpCD <= 0:
			if self.rect.y >= 500:
				player.jump(self)

			if playerPosition[0] - self.rect.x < 0:
				if self.direction == -1:
					if 0 > playerPosition[1] - self.rect.y > -50:
						player.jump(self)
			else:
				if self.direction == 1:
					if 0 > playerPosition[1] - self.rect.y > -50:
						player.jump(self)


		if self.rect.y > playerPosition[1]:
			if self.directionCD <= 0:
				if abs(abs(playerPosition[0]) - abs(self.rect.x)) < 50:
					player.changeDirection(self)
					self.directionCD = 300

	def colliderDetector(self, sprite, ekraan):
		return self.rect.colliderect(sprite)


def startTheGame():

	opponent = enemy()
	print(opponent.rect.x)
	print(opponent.direction)

	a = player()
	clock = pygame.time.Clock()

	while True:
		clock.tick(30)
		event = pygame.event.poll()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				#change direction
				a.changeDirection()

			elif event.key == pygame.K_UP:
				#jump
				a.jump()



		a.nextFramePosition()
		pygame.draw.rect(ekraan, [40, 40, 40], [0, 0, 800, 600], 0)
		ekraan.blit(a.image, (a.rect.x, a.rect.y))
		ekraan.blit(opponent.image, (opponent.rect.x, opponent.rect.y))
		opponent.AI([a.rect.x, a.rect.y])
		opponent.nextFramePosition()

		if opponent.colliderDetector(a, ekraan):
			if opponent.rect.y < a.rect.y:
					tekst = ("YOU LOSE")
					print("w")
			elif opponent.rect.y > a.rect.y:
					tekst = ("YOU WIN")
					print("l")
			pygame.font.init()
			myFont = pygame.font.SysFont("Comic Sans MS", 30)
			textsurface = myFont.render(tekst, False, (220, 220, 0))
			ekraan.blit(textsurface, (100, 100))
			while True:
				import time
				pygame.display.flip()
				time.sleep(5)
				return tekst

		for i in range(len(map)):
			ekraan.blit(porand_pilt, (map[i][0]*20, map[i][1]*20))

		pygame.display.flip()