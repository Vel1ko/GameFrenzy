import pygame
from sys import exit

pygame.init()

# Display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('BoulderBro')
clock = pygame.time.Clock()
test_font = pygame.font.Font('GameFrenzy/Pixeltype.ttf', 50)


backdrop_surface = pygame.image.load('GameFrenzy/backdrop.png')
ground_surface = pygame.image.load('GameFrenzy/ground.png')
text_surface = test_font.render('BoulderBro', False, 'Black')

enemy_surface = pygame.image.load('GameFrenzy/lavaBlurp.png')
enemy_scale = pygame.transform.scale(enemy_surface, (100,100))
enemy_x_pos = 600

#While loop som arbeter med att hålla fönstret öpen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(backdrop_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    screen.blit(text_surface,(300,50))
    enemy_x_pos -= 4
    if enemy_x_pos < -100: enemy_x_pos = 830
    screen.blit(enemy_scale,(enemy_x_pos,225))

    pygame.display.update()
    clock.tick(60)


