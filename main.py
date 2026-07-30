import pgzrun
import random
from pgzero.actor import Actor



def draw():
    screen.blit("background",(0,0))
    mario.draw()
    luigi.draw()

def update():
    pass


WIDTH = 1280
HEIGHT = 720

mario = Actor('mario_right')
mario.x = random.randint(0,WIDTH)
mario.y = random.randint(0,HEIGHT)
luigi = Actor('luigi_right')
luigi.x = random.randint(0,WIDTH)
luigi.y = random.randint(0,HEIGHT)


pgzrun.go()

