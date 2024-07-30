import pygame
from snek import Snek
from food import Food

WIDTH = 360
HEIGHT = 480
FPS = 30
STEP = 10

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snekpy")
clock = pygame.time.Clock()  # For syncing the FPS
update_pos = pygame.USEREVENT+1
pygame.time.set_timer(update_pos, 250)


# Initialize game variables
snek = Snek(WHITE, STEP, WIDTH, HEIGHT)
food = Food.random(WIDTH, HEIGHT, STEP, RED)
queue = []
direction = None


# Game loop
running = True
while running:
    # Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    pygame.event.pump()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # listening for the the X button at the top
            running = False
        if event.type == pygame.KEYDOWN:
            if len(queue) >= 3:
                continue
                
            if direction != 1 and event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                queue.append(0)
            elif direction != 0 and event.key == pygame.K_a or event.key == pygame.K_LEFT:
                queue.append(1)
            elif direction != 3 and event.key == pygame.K_w or event.key == pygame.K_UP:
                queue.append(2)
            elif direction != 2 and event.key == pygame.K_s or event.key == pygame.K_DOWN:
                queue.append(3)
        if event.type == update_pos:
            if len(queue):
                direction = queue.pop(0)
            snek.move(direction)
       
    # Update
    if food.rect.colliderect(snek.segments[0]):
        food = Food.random(WIDTH, HEIGHT, STEP, RED)
        snek.grow()
        
    if snek.segments[0].collidelist(snek.segments[2:]) != -1:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Draw/render
    screen.fill(BLACK)
    snek.draw(screen)
    food.draw(screen)

    # Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()
