import pygame

#zacatek hry
pygame.init()
#vytvoreni obrazovky
sirka = 1100
vyska = 500
screen = pygame.display.set_mode((sirka,vyska))
pygame.display.set_caption("PacMan")
#hlavni cyklus
poracovani = True
while poracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            poracovani = False

#ukonceni  hry
pygame.quit()