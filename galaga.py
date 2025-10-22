import random,pgzrun
#enemies is an empty list
enemies = []
bullets = []
WIDTH,HEIGHT =  1000,600
TITLE = "Galaga game"
#spaceship = Actor makes it an object
spaceship = Actor("galaga")
spaceship.pos = 300,550
spaceship.dead = False
spaceship.countdown = 90
#def draw = define function then draw it
def draw():
    screen.blit("space",(0,0))
    if not spaceship.dead:
      spaceship.draw()
    for b in bullets:
        b.draw()
    for i in enemies:
        i.draw()
# everything inside update makes it so it keeps on updating
def update():
    if not spaceship.dead:
        spaceship.x = spaceship.x + 1
        if keyboard.left:
            spaceship.x -= 10
        if keyboard.right:
            spaceship.x += 10
        if spaceship.x < 0:
            spaceship.x = WIDTH
        if spaceship.x > WIDTH:
            spaceship.x = 0    
    for e in enemies:
        e.y += 5
        for b in bullets:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                break
        if e.colliderect(spaceship):
            spaceship.dead = True
    if spaceship.dead:
        spaceship.countdown -= 1
    if spaceship.countdown == 0:
        spaceship.dead = False
        spaceship.countdown = 90    


    if keyboard.space and not spaceship.dead :
         bullet = Actor("bullet")
         bullet.pos = spaceship.x,spaceship.y-50
         bullets.append(bullet)
    for i in bullets:
        i.y = i.y-10

def create_enemy():
    enemy = Actor("bug")
    enemy.pos = random.randint(50,950),0    
    enemies.append(enemy)
clock.schedule_interval(create_enemy,1.0)     
pgzrun.go()