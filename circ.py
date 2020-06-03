import pygame
import random
import math
class circ():
	def __init__(self, gameDisplay, color, x, y, x_vel, y_vel, radius, id, width, height,mass):
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius
		self.gameDisplay = gameDisplay
		self.width = width
		self.height = height
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.mass = mass
		pygame.draw.circle(self.gameDisplay, self.color, (self.x,self.y), self.radius)


	def move(self):
		self.x += self.x_vel
		self.y += self.y_vel
		pygame.draw.circle(self.gameDisplay, self.color, (int(self.x), int(self.y)), self.radius)

	def reverse_x(self):
		self.x_vel = (-self.x_vel)

	def reverse_y(self):
		self.y_vel = (-self.y_vel)

	def change_vel(self, new_x_vel, new_y_vel):
		self.x_vel = -new_x_vel
		self.y_vel = -new_y_vel

	def calc_angle(self):
		return math.degrees(math.atan2(self.x, self.y))

	def return_coor(self):
		return ((self.x, self.y))

	def hitwall(self):
		if(self.x+self.radius>self.width):
			return "HIT RIGHT"

		elif(self.x-self.radius<0):
			return 'HIT LEFT'

		if(self.y+self.radius>self.height):
			return "HIT DOWN"


		if (self.y-self.radius<0):
			return "HIT UP"
		else:
			return False
