## tasks: 1: threading pressed, 2: Head red, 3: Score appearing,
##        4: Fancy colours, 5: Stationary start
import pygame
import random
import threading

pygame.init()
clock = pygame.time.Clock()

dispx, dispy = 1000, 600
screen = pygame.display.set_mode((dispx, dispy))
done = False
pressed = None

eat = False
lim = 0
curr = 0
growth = 4

x, y = 200, 200
width, height = 40, 40
comp = [(x, y), (x - 40, y), (x - 80, y), (x - 120, y)]
press = ['x', 40]
foodx, foody = 400, 400

colour = (50, 90, 0)
colourin = (10, 30, 140)
     
def rand():
    a = random.randint(0, (dispx/width) - 1) * width
    b = random.randint(0, (dispy/height) - 1) * height
    while (a, b) in comp:
        a = random.randint(0, (dispx/width) - 1) * width
        b = random.randint(0, (dispy/height) - 1) * height
    return a, b
          
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = event.key
        
    if eat == True:
        if press[0] == 'x':
            x += press[1]
        if press[0] == 'y':
            y += press[1]
    elif pressed == pygame.K_UP and press != ('y', 40):
        y -= 40
        press = ('y', -40)
    elif pressed == pygame.K_DOWN and press != ('y', -40):
        y += 40
        press = ('y', 40)
    elif pressed == pygame.K_LEFT and press != ('x', 40):
        x -= 40
        press = ('x', -40)
    elif pressed == pygame.K_RIGHT and press != ('x', -40):
        x += 40
        press = ('x', 40)
    else:
        if press[0] == 'x':
            x += press[1]
        if press[0] == 'y':
            y += press[1]
    
    if (x + width) > dispx or x < 0 or (y + height) > dispy or y < 0:
        break
    
    if (x, y) == (foodx, foody):
        eat = True
        lim += growth
        foodx, foody = rand()

    if curr < lim:
        comp.append((x, y))
        curr += 1
    else:
        eat = False

    for i in range(len(comp) - 1, 0, -1):
        comp[i] = comp[i - 1]
    comp[0] = (x, y)

    screen.fill((0, 0, 0))

    for (a, b) in comp:
        pygame.draw.rect(screen, (10, 0, 0), pygame.Rect(a, b, width, height))
        pygame.draw.rect(screen, colour, pygame.Rect(a + 1, b + 1, width - 2, height - 2))
        pygame.draw.rect(screen, colourin, pygame.Rect(a + 5, b + 5, width - 10, height - 10))
    pygame.draw.rect(screen, (200, 200, 0), pygame.Rect(foodx + 3, foody + 3, width - 6, height - 6))
    
    if(x,y) in comp[1:]:
        break
    
    pygame.display.flip()
    clock.tick(16)


pygame.draw.rect(screen, (10, 0, 0), pygame.Rect(x, y, width, height))
pygame.draw.rect(screen, colour, pygame.Rect(x + 1, y + 1, width - 2, height - 2))
pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(x + 5, y + 5, width - 10, height - 10))
pygame.display.flip()