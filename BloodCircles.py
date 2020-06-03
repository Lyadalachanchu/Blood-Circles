import pygame
import random
import math
from circ import circ
import time

def distance(x1,y1, x2,y2):
	return (math.sqrt((x2-x1)**2+(y2-y1)**2))

def collided(c1, c2):
	return (distance(c1.x, c1.y, c2.x, c2.y)<=c1.radius+c2.radius)

def generator(num):
	l = []
	for i in range(num):
		radiu = random.randint(1,20)
		l.append(circ(gameDisplay,(random.randint(0,255),random.randint(0,1),random.randint(0,25)), 
		random.randint(0,WIDTH),random.randint(0,HEIGHT),random.randint(10,15),random.randint(10,15), radiu, 
		i, WIDTH, HEIGHT, radiu*10))

	return l

def calc_vfx(c1,c2):
	return ((((c1.mass*c1.x_vel)/(c1.mass+c2.mass)+1), ((c2.mass*c2.x_vel)/(c1.mass+c2.mass)+1)))

def calc_vfy(c1,c2):
	return ((((c1.mass*c1.y_vel)/(c1.mass+c2.mass)+1), ((c2.mass*c2.y_vel)/(c1.mass+c2.mass)+1)))




pygame.init()
#WIDTH = 900
#HEIGHT = 700
WIDTH = 600
HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blood Circles")

clock = pygame.time.Clock()

hitWall = False
exit = False

x = 50
y = 50
radius = 20
color = (255,40, 100)

numCircles = 50


l = generator(numCircles)
time.sleep(10)

while not exit:

	for circle in l:
		print(circle.mass)

			
		circle.move()

		if(circle.hitwall() == "HIT DOWN" or circle.hitwall() == "HIT UP"):
			circle.reverse_y()
			
		if(circle.hitwall() == 'HIT LEFT' or circle.hitwall() == 'HIT RIGHT'):
			circle.reverse_x()

	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			exit = True

		print(event)

	pygame.display.update()
	#gameDisplay.fill((0,0,0))
	clock.tick(60)
pygame.quit()
quit()
