import pygame
pygame.init()

#Creating a window

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square Game")

#Creating basic rectangle character
x = 50
y = 50
width = 20
height = 20
vel = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#WASD character movement   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()