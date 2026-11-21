import pygame
from battle import *


pygame.init()
screenLength = 800
screenWidth = 600
screen = pygame.display.set_mode((screenLength, screenWidth))
maxBarLength = 300
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
selection = 0

def drawHpBar(creature, x, y):
    currenthp = creature.currenthp
    maxhp = creature.maxhp
    ratio = currenthp/maxhp
    hpBarLength = round(ratio * maxBarLength)
    if ratio <= 0.2:
        hpColor = (255,0,0)
    elif ratio <= 0.5:
        hpColor = (255,255,0)
    else:
        hpColor = (0,255,0)
        
    pygame.draw.rect(screen, (0,0,0), (x, y, maxBarLength, 100))
    pygame.draw.rect(screen, hpColor, (x, y, hpBarLength, 100))
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flamup.isAlive() and voltile.isAlive():
                    playRound(flamup, flamup.moves[selection], voltile)
            if event.key == pygame.K_UP:
                selection = (selection - 1) % len(flamup.moves)
            if event.key == pygame.K_DOWN:
                selection = (selection + 1) % len(flamup.moves)
            print(f"Selected move: {flamup.moves[selection].name}")
    screen.fill((30,30,30))

    drawHpBar(flamup, 0, 0)
    drawHpBar(voltile, 500, 500)
    creature1text = font.render(f"{flamup.name}: {flamup.currenthp}/{flamup.maxhp}", True, (255,255,255))
    for move in flamup.moves:
        moveBackground = pygame.draw.rect(screen, (50,50,50), (0, 150 + flamup.moves.index(move)*30, 200, 30))
        moveText = font.render(move.name, True, (255,255,255))
        screen.blit(moveText, (5, 155 + flamup.moves.index(move)*30))
    creature2text = font.render(f"{voltile.name}: {voltile.currenthp}/{voltile.maxhp}", True, (255,255,255))
    screen.blit(creature1text, (0,100))
    screen.blit(creature2text,(630,470))
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()