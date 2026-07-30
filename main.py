import random
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def random_location(sprite):
    sprite.x = random.randint(sprite.width//2,WIDTH-sprite.width//2 )
    sprite.y = random.randint(sprite.height//2,HEIGHT-sprite.height//2)

def draw():
    screen.blit("background",(0, 0))
    mario.draw()
    luigi.draw()
    coin.draw()
    screen.draw.text(f"Mario Score: {mario.score}", (10,10), fontsize=30, color="yellow" )
    screen.draw.text(f"Luigi Score: {luigi.score}", (1100,10), fontsize=30, color="yellow" )

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
    if mario.colliderect(coin):
        mario.score += 10
        random_location(coin)

    # Luigi section
    if keyboard.n:
        luigi.x += 5
        luigi.image = "luigi_right"
    if keyboard.m:
        luigi.x += 10
        luigi.image = "luigi_right"
    if keyboard.v:
        luigi.x -= 5
        luigi.image = "luigi_left"
    if keyboard.c:
        luigi.x -= 10
        luigi.image = "luigi_left"
    if keyboard.g:
        luigi.y -= 5
    if keyboard.h:
        luigi.y -= 5
    if keyboard.y:
        luigi.y -= 10
    if keyboard.space:
        luigi.y += 5
    if keyboard.b:
        luigi.y += 10
    if luigi.colliderect(coin):
        luigi.score += 10
        random_location(coin)


WIDTH = 1280
HEIGHT = 720

mario = Actor('mario_right')
random_location(mario)
mario.score = 0

luigi = Actor('luigi_right')
random_location(luigi)
luigi.score = 0

coin = Actor('coin')
random_location(coin)


pgzrun.go()
