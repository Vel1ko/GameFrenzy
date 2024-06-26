  
def boulderBroGame():

    import pygame
    from sys import exit
    from random import randint

    pygame.init()

    # Display
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('BoulderBro')
    clock = pygame.time.Clock()
    spel_font = pygame.font.Font('GameFrenzy/Pixeltype.ttf', 50)
    game_active = False
    start_time = 0
    points = 0

    backdrop_surf = pygame.image.load('GameFrenzy/pixelback.png').convert()
    backdrop_scale = pygame.transform.scale(backdrop_surf, (800,350))
    ground_surf = pygame.image.load('GameFrenzy/groundpixels.png').convert()
    ground_scale= pygame.transform.scale(ground_surf, (800, 400))

    enemy_uno_framo = pygame.image.load('GameFrenzy/lava.png').convert_alpha()
    enemy_scale1 = pygame.transform.scale(enemy_uno_framo, (100,65))
    enemy_dos_framo = pygame.image.load('Gamefrenzy/lava2.png').convert_alpha()
    enemy_scale2 = pygame.transform.scale(enemy_dos_framo, (100,65))
    enemy_framos = [enemy_scale1,enemy_scale2]
    enemy_framo_index = 0
    enemy_surf = enemy_framos[enemy_framo_index]
    enemy_rect = enemy_surf.get_rect(topleft = (600,265))

    cloud_uno_framo = pygame.image.load('GameFrenzy/cloud1.png').convert_alpha()
    cloud_scale1 = pygame.transform.scale(cloud_uno_framo,(100,65))
    cloud_dos_framo = pygame.image.load('GameFrenzy/cloud2.png').convert_alpha()
    cloud_scale2 = pygame.transform.scale(cloud_dos_framo,(100,65))
    cloud_framos = [cloud_scale1, cloud_scale2]
    cloud_framo_index = 0
    cloud_surf = cloud_framos[cloud_framo_index]
    hinder_rect_list = []

    boulder_walk1 = pygame.image.load('GameFrenzy/boulderwalk1.png').convert_alpha()
    boulder_scale1 = pygame.transform.scale(boulder_walk1, (100,100))
    boulder_walk2 = pygame.image.load('GameFrenzy/boulderwalk2.png').convert_alpha()
    boulder_scale2 = pygame.transform.scale(boulder_walk2, (100,100))
    boulder_index = 0
    boulder_walk = [boulder_scale1,boulder_scale2]
    boulder_jump = pygame.image.load('GameFrenzy/boulderjump.png').convert_alpha()
    boulder_jump_scale = pygame.transform.scale(boulder_jump,(100,100))

    boulder_surf = boulder_walk[boulder_index]
    boulder_rect = boulder_scale1.get_rect(topleft = (80,250))

    boulder_gravity = 0

    boulder_stilla = pygame.image.load('Gamefrenzy/boulderbro.png').convert_alpha()
    boulder_stilla_scale = pygame.transform.scale(boulder_stilla, (125,125))
    boulder_stilla_rect = boulder_stilla_scale.get_rect(center = (400,200))

    title_surf = spel_font.render('BoulderBro', False, (0,0,0))
    title_rect = title_surf.get_rect(center = (400,100))


    spel_message = spel_font.render('Press Space To Play', False, (0,0,0))
    spel_message_rect = spel_message.get_rect(center = (400,315))

    hinder_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(hinder_timer, 1500)

    enemy_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_animation_timer,500)

    cloud_animation_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(cloud_animation_timer,300)

    def display_score():
        tiden = int(pygame.time.get_ticks() / 1000) - start_time
        score_surf = spel_font.render(f'Points: {tiden}',False,(64,64,64))
        score_rect = score_surf.get_rect(center =(400,50))
        screen.blit(score_surf,score_rect)
        return tiden

    def hinder_movement(hinder_list):
        if hinder_list:
            for hinder_rect in hinder_list:
                hinder_rect.x -= 6

                if hinder_rect.bottom == 325:
                    screen.blit(enemy_surf, hinder_rect)
                else:
                    screen.blit(cloud_surf, hinder_rect)

            hinder_list =[hinder for hinder in hinder_list if hinder.x > -100]

            return hinder_list
        else:
            return []

    def crash(boulder,hinder):
        if hinder:
            for hinder_rect in hinder:
                if boulder.colliderect(hinder_rect): return False
        return True



    #While loop som arbeter med att hålla fönstret öpen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and boulder_rect.bottom >= 325:
                        boulder_gravity = -20
                
                if game_active:
                    if event.type == hinder_timer:
                        if randint(0,2):
                            hinder_rect_list.append(enemy_surf.get_rect(bottomright = (randint(900,1100), 325)))
                        else:
                            hinder_rect_list.append(cloud_surf.get_rect(bottomright = (randint(900,1100),150)))
                    
                    if event.type == enemy_animation_timer:
                        if enemy_framo_index == 0: enemy_framo_index = 1
                        else: enemy_framo_index = 0
                        enemy_surf = enemy_framos[enemy_framo_index]
                    
                    if event.type == cloud_animation_timer:
                        if cloud_framo_index == 0: cloud_framo_index = 1
                        else: cloud_framo_index = 0
                        cloud_surf = cloud_framos[cloud_framo_index]

                


            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

        

        if game_active:
            screen.blit(backdrop_scale,(0,0))
            screen.blit(ground_scale,(0,250))
            points = display_score()
            
            #Spelare
            boulder_gravity += 0.85
            boulder_rect.y += boulder_gravity
            if boulder_rect.bottom >= 325:
                boulder_rect.bottom = 325
            
            if boulder_rect.bottom < 325:
                boulder_surf = boulder_jump_scale

            else:
                boulder_index += 0.1
                if boulder_index >= len(boulder_walk):
                    boulder_index = 0
                boulder_surf = boulder_walk[int(boulder_index)]

            screen.blit(boulder_surf, boulder_rect)

            #enemy movement
            hinder_rect_list = hinder_movement(hinder_rect_list)

            # death
            game_active = crash(boulder_rect,hinder_rect_list)

        else:
            screen.fill('LightBlue')
            screen.blit(title_surf,title_rect)
            hinder_rect_list.clear()
            boulder_rect.midbottom = (120,250)
            

            points_message = spel_font.render(f'Your points: {points}', False, (0,0,0))
            points_message_rect = points_message.get_rect(center = (400,315))
            screen.blit(boulder_stilla_scale,boulder_stilla_rect)

            if points == 0:    
                screen.blit(spel_message,spel_message_rect)
            else:
                screen.blit(points_message,points_message_rect)


            
        pygame.display.update()
        clock.tick(60)
