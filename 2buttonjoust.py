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



class player:

	def __init__(self):
		self.xPos = 100
		self.yPos = 100
		self.xSpeed = 5
		self.ySpeed = 0
		self.direction = 1

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
		if self.xPos >= 780 and self.direction == 1:
			self.xPos = 0

		elif self.xPos <= 0 and self.direction == -1:
			self.xPos = 780

		self.xPos += self.xSpeed * self.direction
		if self.yPos <= 20 and self.ySpeed < 0:
			self.ySpeed = self.ySpeed * -1

		self.yPos += self.ySpeed
		self.ySpeed += 1

		#todo collision detection and concequenses

class enemy(player):

	def __init__(self):
		player.__init__(self)
		self.xPos = 720
		self.direction = -1
		self.jumpCD = 0 #jump cooldown for AI
		self.directionCD = 0 #direction change cooldown for AI

	def jump(self):
		super().jump()
		self.jumpCD = 300
		print(self.jumpCD)

	def changeDirection(self):
		super().changeDirection()
		self.directionCD = 300
		print(self.directionCD)

	def AI(self, playerPosition):
		self.jumpCD -= 1
		self.directionCD -=1

		if self.jumpCD <= 0:
			if self.yPos >= 500:
				player.jump(self)

			if playerPosition[0] - self.xPos < 0:
				if self.direction == -1:
					if 0 > playerPosition[1] - self.yPos > -50:
						player.jump(self)
			else:
				if self.direction == 1:
					if 0 > playerPosition[1] - self.yPos > -50:
						player.jump(self)


		if self.yPos > playerPosition[1]:
			if self.directionCD <= 0:
				if abs(abs(playerPosition[0]) - abs(self.xPos)) < 50:
					player.changeDirection(self)
					self.directionCD = 300


opponent = enemy()
print(opponent.xPos)
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
	ekraan.blit(player_pilt, (a.xPos, a.yPos))
	ekraan.blit(enemy_pilt, (opponent.xPos, opponent.yPos))
	opponent.AI([a.xPos, a.yPos])
	opponent.nextFramePosition()
	for i in range(len(map)):
		ekraan.blit(porand_pilt, (map[i][0]*20, map[i][1]*20))

	pygame.display.flip()