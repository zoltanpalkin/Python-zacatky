#udelat pacmana
import pygame

pygame.init()



sirka = 1500
vyska = 800



screen  = pygame.display.set_mode((sirka,vyska))
pygame.display.set_caption("PacMan")


#zvuky
zvuk_zacatek = pygame.mixer.Sound("hry/assety/zvuky/pacman_beginning.wav")
zvuk_zacatek.play()
# barvy

black = (0,0,0)
yellow = (240,220,20)
neon_blue = (25,25,166)
screen.fill(black)

# nastaveni
distance = 5
fps = 60


#nadpisy
custom_font = pygame.font.Font("hry/assety/fonty/pacfont.ttf" ,60)

custom_text = custom_font.render("PACMAN", True, yellow)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (750, 45)

skore_text = custom_font.render("SKORE", True, yellow)
skore_text_rect = skore_text.get_rect()
skore_text_rect.center = (150, 45)


up_text = custom_font.render("1UP", True, yellow)
up_text_rect = up_text.get_rect()
up_text_rect.center = (1400, 45)
#postavy
#animace
image_sprite = [pygame.image.load("hry/assety/obrazky/pacman.png"),
                pygame.image.load("hry/assety/obrazky/pacman2.png")]
clock = pygame.time.Clock()

pacman_main_char = pygame.image.load("hry/assety/obrazky/pacman.png")
pacman_main_char = pygame.transform.scale(pacman_main_char, (50, 50))
pacman_main = pacman_main_char.get_rect()
pacman_main.center = (100, 200)

dot_main_char = pygame.image.load("hry/assety/obrazky/dot.png")
dot_main_char = pygame.transform.scale(dot_main_char, (10, 10))
dot_main = dot_main_char.get_rect()
dot_main.center = (300, 500)

#tvary

pygame.draw.line(screen, yellow, (0,0), (sirka//2,vyska//2), 3)
pygame.draw.line(screen, yellow, (0,0), (sirka//2,vyska//2), 3)
#pygame.draw.circle(screen, yellow, (vyska//2,sirka//2), 200 ,10)
pygame.draw.rect(screen, neon_blue , (100,0,50,100,),2)
pokracovani = True
while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False
    keys = pygame.key.get_pressed()
    screen.fill(black)
    pygame.draw.line(screen, yellow, (0,75), (1500,75), 3)
    clock = pygame.time.Clock()

    if keys [pygame.K_UP]:
        pacman_main.y -= distance
    elif keys [pygame.K_DOWN]:
        pacman_main.y += distance
    elif keys [pygame.K_RIGHT]:
        pacman_main.x += distance
    elif keys [pygame.K_LEFT]:
        pacman_main.x -= distance
    
    screen.blit(pacman_main_char, pacman_main)
    screen.blit(dot_main_char, dot_main)
    screen.blit(custom_text, custom_text_rect)
    screen.blit(skore_text, skore_text_rect)
    screen.blit(up_text, up_text_rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()