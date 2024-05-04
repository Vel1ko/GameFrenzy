import pygame
from sys import exit

pygame.init()

# Display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('BoulderBro')
clock = pygame.time.Clock()
test_font = pygame.font.Font('GameFrenzy/Pixeltype.ttf', 50)
game_active = True

backdrop_surf = pygame.image.load('GameFrenzy/pixelback.png').convert()
backdrop_scale = pygame.transform.scale(backdrop_surf, (800,350))
ground_surf = pygame.image.load('GameFrenzy/ground.png').convert()

score_surf = test_font.render('BoulderBro', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

enemy_surf = pygame.image.load('GameFrenzy/lavaBlurp.png').convert_alpha()
enemy_scale = pygame.transform.scale(enemy_surf, (100,65))
enemy_rect = enemy_scale.get_rect(topleft = (600,300))

boulder_surf = pygame.image.load('GameFrenzy/').convert_alpha()
boulder_scale = pygame.transform.scale(boulder_surf, (100,100))
boulder_rect = boulder_scale.get_rect(topleft = (80,250))
boulder_gravity = 0

#While loop som arbeter med att hålla fönstret öpen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boulder_rect.collidepoint(event.pos) and  boulder_rect.bottom >= 350:
                    boulder_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and boulder_rect.bottom >= 350:
                    boulder_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 800

    if game_active:
        screen.blit(backdrop_scale,(0,0))
        screen.blit(ground_surf,(0,250))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen, '#c0e8ec',score_rect,75)
        screen.blit(score_surf,(score_rect))

        enemy_rect.left -= 4
        if enemy_rect.left < -100: enemy_rect.left = 850
        screen.blit(enemy_scale,enemy_rect)
        
        #Spelare
        boulder_gravity += 1
        boulder_rect.y += boulder_gravity
        if boulder_rect.bottom >= 350:
            boulder_rect.bottom = 350
        screen.blit(boulder_scale, boulder_rect)

        # death
        if enemy_rect.colliderect(boulder_rect):
            game_active = False
    else:
        screen.fill('LightBlue')


        
    pygame.display.update()
    clock.tick(60)


