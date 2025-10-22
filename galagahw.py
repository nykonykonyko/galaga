import random,pgzrun
enemies = []
WIDTH,HEIGHT =  1000,600
TITLE = "Galaga game"
character = Actor("shinji")
character.pos = 300,550
def draw():
    screen.blit("space",(0,0))
    character.draw()
    for i in enemies:
        i.draw()
def update():
    character.x = character.x + 1
    if keyboard.left:
        character.x -= 10
    if keyboard.right:
        character.x += 10
    if character.x < 0:
        character.x = WIDTH
    if character.x > WIDTH:
        character.x = 0
    character.y = character.y + 1
    if keyboard.up:
        character.y -= 10
    if keyboard.down:
        character.y += 10
    if character.y < 0:
        character.y = HEIGHT
    if character.y > HEIGHT:
        character.y = 0            
    enemy = Actor("bug")
    enemy.pos = random.randint(50,950),0    
    enemies.append(enemy)

pgzrun.go()