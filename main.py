import random
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def random_location(sprite):
    sprite.x = random.randint(sprite.width//2,WIDTH-sprite.width//2 )
    sprite.y = random.randint(sprite.height//2,HEIGHT-sprite.height//2)

def on_key_down():
    global status
    if keyboard.space:
        status = "play"

def draw():
    if status == "home":
        screen.blit("home", (0, 0))
    elif status == "play":
        screen.blit("background",(0, 0))
        mario.draw()
        luigi.draw()
        coin.draw()
        screen.draw.text(f"Mario Score: {mario.score}", (10,10), fontsize=30, color="yellow" )
        screen.draw.text(f"Luigi Score: {luigi.score}", (1100,10), fontsize=30, color="yellow" )

def update():
    if status == "play":
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
        if luigi.colliderect(coin):
            luigi.score += 10
            random_location(coin)


WIDTH = 1280
HEIGHT = 720

status = "home"

mario = Actor('mario_right')
random_location(mario)
mario.score = 0

luigi = Actor('luigi_right')
random_location(luigi)
luigi.score = 0

coin = Actor('coin')
random_location(coin)


pgzrun.go()
