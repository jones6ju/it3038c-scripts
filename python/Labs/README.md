For this lab I used the Pygame plugin that is used for creating games.

Run the Lab7.py file and a window titled "Square Game" should open.


The First task you can complete is creating a game window:


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square Game")


Another Task is coding a basic character, in this case a simple rectangle.
First give the starting position in x,y and then the size and velocity of the character


x = 50
y = 50
width = 20
height = 20
vel = 10


The 3rd task is programming the character movement events to specific keys, in this case 'WASD'


keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_s]:
        y += vel
