import pgzrun
import random
from pgzero.actor import Actor
from pgzero.keyboard import keyboard



def draw():
    screen.blit("background",(0,0))
    mario.draw()
    luigi.draw()

def update():
    # Mario section
    if keyboard.right:
        mario.x += 5
        mario.image = "mario_right"
    if keyboard.left:
        mario.x -= 5
        mario.image = "mario_left"
    if keyboard.up:
        mario.y -= 5
    if keyboard.down:
        mario.y += 5
    
    # Luigi section
    if keyboard.s:
        luigi.x += 5
        luigi.image = "luigi_right"
    if keyboard.a:
        luigi.x -= 5
        luigi.image = "luigi_left"
    if keyboard.w:
        luigi.y -= 5
    if keyboard.z:
        luigi.y += 5


WIDTH = 1280
HEIGHT = 720

mario = Actor('mario_right')
mario.x = random.randint(0,WIDTH)
mario.y = random.randint(0,HEIGHT)
luigi = Actor('luigi_right')
luigi.x = random.randint(0,WIDTH)
luigi.y = random.randint(0,HEIGHT)


pgzrun.go()

