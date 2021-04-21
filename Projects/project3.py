import pygame
from pygame.constants import K_SPACE
pygame.init()

#Creating a window

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square Game")

#Creating basic rectangle character

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.whenJump = False
        self.countJump = 10
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draw(self,win):
        self.hitbox = (self.x, self.y, 50, 50)
        pygame.draw.rect(win, (0,255,0), self.hitbox)
    
        
#Creating basic rectangular enemies

class platform(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 70, 70)
    
    def draw(self, win):
        self.hitbox = (self.x, self.y, 70, 70)
        pygame.draw.rect(win, (255,0,0), (plat.x, plat.y, plat.width, plat.height))
        pygame.draw.rect(win, (255,0,0), (plat2.x, plat2.y, plat2.width, plat2.height))
        pygame.draw.rect(win, (0,0,255), (plat3.x, plat3.y, plat3.width, plat3.height))
        pygame.draw.rect(win, (0,0,255), (plat4.x, plat4.y, plat4.width, plat4.height))


# defining object start positions

plat = platform(100, 430, 70, 70)
plat2 = platform(250, 430, 70, 70)
plat3 = platform(430, 350, 70, 70)
plat4 = platform(250, 200, 70, 70)
square = player(0, 450, 50, 50)
run = True

#main (character movement and interaction)

while run:
    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


### Lines 70 -89 are my attempt at adding collision so the player won't pass through the platform when jumping on it
### The idea was take the bottom of the player (square) and moving the player up if the bottom of the square was lower than the
##  top of the platform. However, this kept causing the game to crash and I couldn't get it figured out.

#    for square in player:
#       if square.x + square.width >= plat.x:
#            square.x = plat.x - 50
#        if square.y + square.height >= plat.y:
#            square.y = plat.y - 50
#        
#        if square.x + square.width >= plat2.x:
#            square.x = plat2.x - 50
#        if square.y + square.height >= plat2.y:
#            square.y = plat2.y - 50
#        
#        if square.x + square.width >= plat3.x:
#            square.x = plat3.x - 50
#        if square.y + square.height >= plat3.y:
#            square.y = plat3.y - 50
#
#        if square.x + square.width >= plat4.x:
#            square.x = plat4.x - 50
#        if square.y + square.height >= plat4.y:
#            square.y = plat4.y - 50

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and square.x > square.vel:
        square.x -= square.vel
    if keys[pygame.K_d] and square.x < 450:
        square.x += square.vel
    if not (square.whenJump): 
        if keys[pygame.K_SPACE]:
            square.whenJump = True
    else:
        if square.countJump >= -10:
            negative = 1
            if square.countJump < 0:
                negative = -1
            square.y -= (square.countJump ** 2) /2 * negative
            square.countJump -= 1
        else:
            square.whenJump = False
            square.countJump = 10
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (square.x, square.y, square.width, square.height))
    pygame.draw.rect(win, (255,0,0), (plat.x, plat.y, plat.width, plat.height))
    pygame.draw.rect(win, (255,0,0), (plat2.x, plat2.y, plat2.width, plat2.height))
    pygame.draw.rect(win, (0,0,255), (plat3.x, plat3.y, plat3.width, plat3.height))
    pygame.draw.rect(win, (0,0,255), (plat4.x, plat4.y, plat4.width, plat4.height))
    pygame.display.update()

pygame.quit()