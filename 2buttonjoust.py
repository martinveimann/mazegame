#2 button flappyJoust

import pygame
import time

ekraan = pygame.display.set_mode((800, 600))


porand_pilt = pygame.image.load("sein.png")
player_pilt = pygame.image.load("uus_kast.png")
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
		self.ySpeed = -10

	def changeDirection(self):
		self.direction = self.direction * -1
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
	for i in range(len(map)):
		ekraan.blit(porand_pilt, (map[i][0]*20, map[i][1]*20))
	pygame.display.flip()